class BalanceException(Exception):
    pass


class BankAccount:
    
    def __init__(self, initialAmount, accountName):
        self.balance = initialAmount
        self.name = accountName
        print(f"\nAccount '{self.name}' Created. \nBalance = ${self.balance:.2f}")

    def getBalance(self):
        '''Input: None   Output: Prints Current Balance'''

        print(f"\nAccount '{self.name}' Current Balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit Completed.")
        self.getBalance()

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\n Withdrawal Complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self,amount,account):
        try:
            print("\n**********\n\n Beginning Transfer 🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete! ✅ \n\n***********")
        except BalanceException as error:
            print(f'\nTransfer interrupted. ❌ {error}')
