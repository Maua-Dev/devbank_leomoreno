from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.transaction_type_enum import TransactionTypeEnum

class Transaction:
    transaction_type: TransactionTypeEnum
    value: float
    current_balance: float
    timestamp: float

    def __init__(self, transaction_type: TransactionTypeEnum = None, value: float = None, current_balance: float = None, timestamp: float = None):
        validation_type = self.validate_transaction_type(transaction_type)
        if validation_type[0] is False:
            raise ParamNotValidated("transaction_type", validation_type[1])
        self.transaction_type = transaction_type

        validation_value = self.validate_value(value)
        if validation_value[0] is False:
            raise ParamNotValidated("value", validation_value[1])
        self.value = value

        validation_balance = self.validate_current_balance(current_balance)
        if validation_balance[0] is False:
            raise ParamNotValidated("current_balance", validation_balance[1])
        self.current_balance = current_balance

        validation_timestamp = self.validate_timestamp(timestamp)
        if validation_timestamp[0] is False:
            raise ParamNotValidated("timestamp", validation_timestamp[1])
        self.timestamp = timestamp

    @staticmethod
    def validate_transaction_type(transaction_type: TransactionTypeEnum) -> Tuple[bool, str]:
        if transaction_type is None:
            return (False, "Transaction type is required")
        if type(transaction_type) != TransactionTypeEnum:
            return (False, "Transaction type must be a TransactionTypeEnum")
        return (True, "")

    @staticmethod
    def validate_value(value: float) -> Tuple[bool, str]:
        if value is None:
            return (False, "Value is required")
        if type(value) != float:
            return (False, "Value must be a float")
        if value <= 0:
            return (False, "Value must be greater than 0")
        return (True, "")

    @staticmethod
    def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
        if current_balance is None:
            return (False, "Current balance is required")
        if type(current_balance) != float:
            return (False, "Current balance must be a float")
        return (True, "")

    @staticmethod
    def validate_timestamp(timestamp: float) -> Tuple[bool, str]:
        if timestamp is None:
            return (False, "Timestamp is required")
        if type(timestamp) != float:
            return (False, "Timestamp must be a float")
        return (True, "")

    def to_dict(self):
        return {
            "transaction_type": self.transaction_type.value,
            "value": self.value,
            "current_balance": self.current_balance,
            "timestamp": self.timestamp
        }

    def __eq__(self, other):
        return (self.transaction_type == other.transaction_type and
                self.value == other.value and
                self.current_balance == other.current_balance and
                self.timestamp == other.timestamp)

    def __repr__(self):
        return f"Transaction(transaction_type={self.transaction_type}, value={self.value}, current_balance={self.current_balance}, timestamp={self.timestamp})"
