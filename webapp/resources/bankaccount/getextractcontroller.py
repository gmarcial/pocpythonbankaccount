import json
from webapp import app
from webapp.utils.enconder import CustomEncoder
from flask import request, Response
from app.financemanagement.UseCases.getextract import GetExtract


@app.route('/bankaccounts/<string:accountnumber>/banktransactionrecords', methods=["GET"])
def getextract(accountnumber):

    usecase = GetExtract()
    response = None
    bankaccount = usecase.execute(accountnumber)
    bankaccountjson = json.dumps(bankaccount, cls=CustomEncoder)
    response = Response(bankaccountjson, 200, mimetype="application/json")
    #try:
    #    bankaccount = usecase.execute(accountnumber)
    #    bankaccountjson = json.dumps(bankaccount, cls=CustomEncoder)
    #    response = Response(bankaccountjson, 200, mimetype="application/json")
    #except Exception:
    #    response = Response("Ocorreu um erro ao tentar recuperar a conta bancaria", 500)

    return response
