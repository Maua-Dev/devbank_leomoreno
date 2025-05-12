from abc import ABC, abstractmethod
from typing import List, Optional

from ..entities.user import User

class IUserRepository(ABC):

    @abstractmethod
    def get_all_users(self) -> List[User]:
        """Returns all users in the database"""
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> Optional[User]:
        """Returns the user with the given id. If not found, returns None"""
        pass

    @abstractmethod
    def create_user(self, user: User, user_id: int) -> User:
        """Creates a new user"""
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> Optional[User]:
        """Deletes the user with the given id. Returns the deleted user or None"""
        pass

    @abstractmethod
    def update_user(
        self,
        user_id: int,
        name: str = None,
        agency: str = None,
        account: str = None,
        current_balance: float = None
    ) -> Optional[User]:
        """Updates the user info. Returns the updated user or None"""
        pass
