from ..entities.account import Account

class AccountRepository:
    def __init__(self):
        self.accounts = {}  # Usando um dicionário para armazenar contas

    def add(self, account: Account):
        if account.account in self.accounts:
            raise ValueError("Account already exists")
        self.accounts[account.account] = account

    def get(self, account_number: str):
        return self.accounts.get(account_number, None)

    def deposit(self, account_number: str, amount: float):
        account = self.get(account_number)
        if not account:
            raise ValueError("Account not found")
        account.deposit(amount)
        return account
