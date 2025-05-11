class Account:
    def __init__(self, name: str, agency: str, account: str, current_balance: float):
        self.name = name
        self.agency = agency
        self.account = account
        self.current_balance = current_balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.current_balance += amount

    def to_dict(self):
        return {
            "name": self.name,
            "agency": self.agency,
            "account": self.account,
            "current_balance": self.current_balance
        }
