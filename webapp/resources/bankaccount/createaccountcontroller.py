from webapp import app
from flask import request, Response, jsonify
from app.financemanagement.UseCases.createbankaccount import CreateBankAccount

@app.route('/bankaccounts', methods=["POST"])
def createbankaccount():
    
    payload = request.get_json(cache=False)
    balance = payload['balance']
    accounttype = payload['accounttype']
    
    usecase = CreateBankAccount()
    
    response = None
    
    try:
        usecase.execute(balance, accounttype)
        response = Response("A conta bancaria foi criada com sucesso", 200)
    except Exception:
        response = Response("Ocorreu um erro ao tentar criar uma conta bancaria", 500)
    
    return response