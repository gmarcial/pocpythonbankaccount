from webapp import app
from flask import request, Response
from app.financemanagement.UseCases.totransfer import ToTransfer

@app.route('/bankaccounts/totransfer', methods=["PUT"])
def totransfer():
    
    payload = request.get_json(cache=False)
    senderaccountnumber = payload['senderaccountnumber']
    receiveraccountnumber = payload['receiveraccountnumber']
    transferamount = payload['transferamount']
    
    usecase = ToTransfer()
    
    response = None
    try:
        usecase.execute(senderaccountnumber, receiveraccountnumber, transferamount)
        response = Response("A transferencia ocorreu com sucesso.", 200)
    except Exception:
        response = Response("Ocorreu um erro ao tentar realizar a transferencia.", 500)
    
    return response