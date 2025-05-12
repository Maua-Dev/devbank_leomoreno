from typing import Dict, Optional, List

from ..entities.transaction import Transaction
from ..enums.transaction_type_enum import TransactionTypeEnum
from .transaction_repository_interface import ITransactionRepository


class TransactionRepositoryMock(ITransactionRepository):
    transactions: Dict[int, Transaction]

    def __init__(self):
        self.transactions = {
        }

    def get_all_transactions(self) -> List[Transaction]:
        return list(self.transactions.values())

    def get_transaction(self, transaction_id: int) -> Optional[Transaction]:
        return self.transactions.get(transaction_id)

    def create_transaction(self, transaction: Transaction, transaction_id: int) -> Transaction:
        self.transactions[transaction_id] = transaction
        return transaction

    def delete_transaction(self, transaction_id: int) -> Optional[Transaction]:
        return self.transactions.pop(transaction_id, None)

    def update_transaction(
        self,
        transaction_id: int,
        transaction_type: TransactionTypeEnum = None,
        value: float = None,
        current_balance: float = None,
        timestamp: float = None
    ) -> Optional[Transaction]:
        transaction = self.transactions.get(transaction_id)
        if not transaction:
            return None

        if transaction_type is not None:
            transaction.transaction_type = transaction_type
        if value is not None:
            transaction.value = value
        if current_balance is not None:
            transaction.current_balance = current_balance
        if timestamp is not None:
            transaction.timestamp = timestamp

        self.transactions[transaction_id] = transaction
        return transaction
