from bank_accounts import *

Utkarsh = BankAccount(1000, "Utkarsh")
Akarsh = BankAccount(2000, "Akarsh")

Utkarsh.getBalance()
Akarsh.getBalance()

Utkarsh.deposit(150)
Akarsh.withdraw(1000)

Utkarsh.transfer(10000,Akarsh)
Utkarsh.transfer(100,Akarsh)