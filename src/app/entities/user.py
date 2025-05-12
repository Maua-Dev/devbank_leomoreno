from typing import Tuple
from ..errors.entity_errors import ParamNotValidated

class User:
    name: str
    agency: str  # Ex: "0000"
    account: str  # Ex: "00000-0"
    current_balance: float

    def __init__(self, name: str = None, agency: str = None, account: str = None, current_balance: float = None):
        validation_name = self.validate_name(name)
        if not validation_name[0]:
            raise ParamNotValidated("name", validation_name[1])
        self.name = name

        validation_agency = self.validate_agency(agency)
        if not validation_agency[0]:
            raise ParamNotValidated("agency", validation_agency[1])
        self.agency = agency

        validation_account = self.validate_account(account)
        if not validation_account[0]:
            raise ParamNotValidated("account", validation_account[1])
        self.account = account

        validation_balance = self.validate_current_balance(current_balance)
        if not validation_balance[0]:
            raise ParamNotValidated("current_balance", validation_balance[1])
        self.current_balance = current_balance

    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return False, "Name is required"
        if not isinstance(name, str):
            return False, "Name must be a string"
        if len(name.strip()) < 3:
            return False, "Name must be at least 3 characters long"
        return True, ""

    @staticmethod
    def validate_agency(agency: str) -> Tuple[bool, str]:
        if agency is None:
            return False, "Agency is required"
        if not isinstance(agency, str):
            return False, "Agency must be a string"
        if len(agency) != 4 or not agency.isdigit():
            return False, "Agency must be a 4-digit string"
        return True, ""

    @staticmethod
    def validate_account(account: str) -> Tuple[bool, str]:
        if account is None:
            return False, "Account is required"
        if not isinstance(account, str):
            return False, "Account must be a string"
        if not account[:-2].isdigit() or account[-2] != '-' or not account[-1].isdigit():
            return False, "Account must follow the format '00000-0'"
        return True, ""

    @staticmethod
    def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
        if current_balance is None:
            return False, "Current balance is required"
        if not isinstance(current_balance, float):
            return False, "Current balance must be a float"
        if current_balance < 0:
            return False, "Current balance cannot be negative"
        return True, ""

    @staticmethod
    def validate_user_id(user_id: int) -> Tuple[bool, str]:
        if user_id is None:
            return False, "Missing 'user_id' parameter"
        if not isinstance(user_id, int):
            return False, "User ID must be an integer"
        if user_id < 0:
            return False, "User ID must be a positive integer"
        return True, ""

    def to_dict(self):
        return {
            "name": self.name,
            "agency": self.agency,
            "account": self.account,
            "current_balance": self.current_balance
        }

    def __eq__(self, other):
        return (
            self.name == other.name and
            self.agency == other.agency and
            self.account == other.account and
            self.current_balance == other.current_balance
        )

    def __repr__(self):
        return (
            f"User(name={self.name}, agency={self.agency}, "
            f"account={self.account}, current_balance={self.current_balance})"
        )
