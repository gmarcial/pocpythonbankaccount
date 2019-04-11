from webapp import app
from flask import request, Response
from app.financemanagement.UseCases.towithdraw import ToWithdraw

@app.route('/bankaccounts/<string:accountnumber>/towithdraw', methods=["PUT"])
def towithdraw(accountnumber):
    
    payload = request.get_json(cache=False)
    withdrawamount = payload['withdrawamount']
    
    usecase = ToWithdraw()

    response = None
    try:
        usecase.execute(accountnumber, withdrawamount)
        response = Response("O saque ocorreu com sucesso.", 200)
    except Exception:
        response = Response("Ocorreu um erro ao tentar realizar o saque.", 500)
    
    return response