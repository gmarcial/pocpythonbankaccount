from flask import Flask

app = Flask(__name__)

from webapp.resources.bankaccount import createaccountcontroller
from webapp.resources.bankaccount import getallbankaccountcontroller
from webapp.resources.bankaccount import getbankaccountcontroller
from webapp.resources.bankaccount import todepositcontroller
from webapp.resources.bankaccount import towithdrawcontroller
from webapp.resources.bankaccount import totransfercontroller
from webapp.resources.bankaccount import getextractcontroller

app.run(debug=True)