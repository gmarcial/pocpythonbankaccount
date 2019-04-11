from webapp import app
from flask import request, Response
from app.financemanagement.UseCases.todeposit import ToDeposit

@app.route('/bankaccounts/<string:accountnumber>/todeposit', methods=["PUT"])
def todeposit(accountnumber):
    
    payload = request.get_json(cache=False)
    depositamount = payload['depositamount']
    
    usecase = ToDeposit()

    response = None
    try:
        usecase.execute(accountnumber, depositamount)
        response = Response("O deposito ocorreu com sucesso.", 200)
    except Exception:
        response = Response("Ocorreu um erro ao tentar realizar o deposito.", 500)
    
    return response