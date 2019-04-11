# POC: Python - Bank account

This project has the objective of use and demonstrate the python use in practice.

## Stack used:
> 
* Python 3.6.8
* Flask 1.0.2
* SQLAlchemy 1.3.2
* SQLite 3
>

## Structure resume:

```
project    
│
└───app
│   │   
│   └───financemanagement
|       |
|       └───bankingoperation
|       |
|       └───infrasctructure
|       |
|       └───usecases
|       |
|       └───tests
│   
└───webapp
    |
    └───resources
        |
        └───bankaccount
```

All start in the package [app], where the modules of the software are implemented, in our case, [financemanagement].

Each module contains your own architecture, making it decoupled and independent, according to your necessity and complexity.

### In our sample:

```
[bankingoperation] => Sub-package, implementation the banking operations
[infrasctructure] => Foundation base of the module, as the persistence of the data.
[usecases] => Segregation and communication the objects responsibles for the realization of one of the feature / behavior of that module.
[tests] => unittests
```

The main means of communication is through the HTTP protocol, where the package [webapp] is responsible therefore.

### In our sample:

```
[resources] => Sub-package, implemented the resources of the software modules as [bankaccount] through controllers.
[utils] => Auxiliaries recourses for the modules of package [webapp]
```

## Ports and Adapter concepts:

Maintain the segregation of responsibility between the architecture parts, how the modules, not leaking out behavior and mainly generate a very weak accouplement between them and yes modularize.

That all to fortalice the limit delimited between contexts.

>
https://www.thinktocode.com/2018/07/19/ports-and-adapters-architecture/
>

### In our sample:

```
[ports] => Controllers, that do not know low level modules how [bankaccount], but yes high level how usecase [todeposit].
[adapters] 
{
    Everything that is external to the rules/requiriments of the software modules, 
    an interface defined to represent a behavior expected by rule a module, 
    adapters to this behavior should implement the same to execution.

    Ex:
        Behavior expected [repository]: add(), update(), find()
        Bahavior in SQLAlchemy adapter [repository]: add(), update(), find()...

    Different from static languages, python for being dynamic, implements interfaces (to IOC) of form explicit, thanks to interpretation.

    You define the behavior expected, soon the obj used should corresponding, else don't function.

}
```


# Resources:

[BankAccount]

<details><summary>Create bank account</summary>
<p>

```
Endpoint: /bankaccounts
Http verb: POST
Payload sample:
{
	"balance": 100,
	"accounttype": 1
}
```
</p>
</details>

<details><summary>Get all bank accounts</summary>
<p>

```
Endpoint: /bankaccounts
Http verb: GET
Not payload
```
</p>
</details>

<details><summary>Get bank accounts</summary>
<p>

```
Endpoint: /bankaccounts/account_number
Http verb: GET
Not payload
```
</p>
</details>

<details><summary>To deposit</summary>
<p>

```
Endpoint: /bankaccounts/account_number/todeposit
Http verb: PUT
Payload sample:
{
	"depositamount": 1000
}
```
</p>
</details>

<details><summary>To withdraw</summary>
<p>

```
Endpoint: /bankaccounts/account_number/towithdraw
Http verb: PUT
Payload sample:
{
	"withdrawamount": 100
}
```
</p>
</details>

<details><summary>To transfer</summary>
<p>

```
Endpoint: /bankaccounts/totransfer
Http verb: PUT
Payload sample:
{
	"senderaccountnumber": "453597448782153408",
	"receiveraccountnumber": "199500548873012934",
	"transferamount": 100
}
```
</p>
</details>

<details><summary>Get extract</summary>
<p>

```
Endpoint: /bankaccounts/account_number/banktransactionrecords
Http verb: GET
Not payload
```
</p>
</details>

# Run application:

For installing all dependencies of the project:
>
    pip install -r requirements.txt in your shell.
>

The bank is a SQLITE, check if there is a file representing the database, named: bank.db

If exist, open and check if exists the tables [BankAccount] and [BankTransactionRecord], case have, next, else, open the file [scripts.sql] and create.

NOTE: I suggest use DBbrowser sqlite for the database management.

If all is ok, run:
>
    python run.py
>