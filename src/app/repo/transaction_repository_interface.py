from abc import ABC, abstractmethod
from typing import List, Optional

from ..entities.transaction import Transaction
from ..enums.transaction_type_enum import TransactionTypeEnum


class ITransactionRepository(ABC):

    @abstractmethod
    def get_all_transactions(self) -> List[Transaction]:
        """Returns all transactions in the database"""
        pass

    @abstractmethod
    def get_transaction(self, transaction_id: int) -> Optional[Transaction]:
        """Returns the transaction with the given id. If not found, returns None"""
        pass

    @abstractmethod
    def create_transaction(self, transaction: Transaction, transaction_id: int) -> Transaction:
        """Creates a new transaction"""
        pass

    @abstractmethod
    def delete_transaction(self, transaction_id: int) -> Optional[Transaction]:
        """Deletes the transaction with the given id. Returns the deleted transaction or None"""
        pass

    @abstractmethod
    def update_transaction(
        self,
        transaction_id: int,
        transaction_type: TransactionTypeEnum = None,
        value: float = None,
        current_balance: float = None,
        timestamp: float = None
    ) -> Optional[Transaction]:
        """Updates the transaction info. Returns the updated transaction or None"""
        pass
