CREATE TABLE BankAccount(
	Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Number String NOT NULL UNIQUE,
	Balance DECIMAL NOT NULL,
	Type INTEGER NOT NULL
);

CREATE TABLE BankTransactionRecord(
	Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Operation INTEGER NOT NULL,
	Number String NOT NULL,
	WhenCccurred DateTime NOT NULL,
	Amount Decimal NOT NULL,
	Description String(100) NOT NULL,
	ContaId INTEGER NOT NULL,
	FOREIGN KEY (ContaId) REFERENCES BankAccount (Id)
	);