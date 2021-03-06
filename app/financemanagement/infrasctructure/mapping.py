from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey

MapBase = declarative_base()


class BankAccountMap(MapBase):

    __tablename__ = 'BankAccount'

    id = Column('Id', Integer, primary_key=True, nullable=False)
    number = Column('Number', String(150), nullable=False, unique=True)
    balance = Column('Balance', DECIMAL, nullable=False)
    type = Column('Type', Integer, nullable=False)

class BankAccountModel():
    def __init__(self, id, number, balance, type):
        self.id = id
        self.number = number
        self.balance = balance
        self.type = type


class BankTransactionRecordMap(MapBase):

    __tablename__ = 'BankTransactionRecord'

    id = Column('Id', Integer, primary_key=True, nullable=False)
    operation = Column('Operation', Integer, nullable=False)
    number = Column('Number', String(150), nullable=False)
    whenoccurred = Column('WhenCccurred', DateTime, nullable=False)
    amount = Column('Amount', DECIMAL, nullable=False)
    description = Column('Description', String(100), nullable=False)
    contaid = Column('ContaId', Integer, ForeignKey(
        "BankAccount.Id"), nullable=False)

class BankTransactionRecordModel():
    def __init__(self, id, operation, number, whenoccurred, amount, description, contaid):
        self.id = id
        self.operation = operation
        self.number = number
        self.whenoccurred = whenoccurred
        self.amount = amount
        self.description = description
        self.contaid = contaid