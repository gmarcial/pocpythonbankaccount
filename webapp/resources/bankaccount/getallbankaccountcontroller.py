import json
from webapp import app
from webapp.utils.enconder import CustomEncoder
from flask import request, Response
from app.financemanagement.UseCases.getallbankaccount import GetAllBankAccount


@app.route('/bankaccounts', methods=["GET"])
def getallbankaccount():

    usecase = GetAllBankAccount()

    response = None
    try:
        bankaccountlist = usecase.execute()
        bankaccountjson = json.dumps(bankaccountlist, cls=CustomEncoder)
        response = Response(bankaccountjson, 200, mimetype="application/json")
    except Exception:
        response = Response("Ocorreu um erro ao tentar recuperar todas contas bancarias", 500)

    return response
