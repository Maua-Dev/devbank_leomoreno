from typing import Dict, Optional, List

from ..entities.user import User
from .user_repository_interface import IUserRepository


class UserRepositoryMock(IUserRepository):
    users: Dict[int, User]

    def __init__(self):
        self.users = {
            1: User(name="Leonardo Moreno", agency="6331", account="16090-0", current_balance=3000.0)
        }

    def get_all_users(self) -> List[User]:
        return list(self.users.values())

    def get_user(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id)

    def create_user(self, user: User, user_id: int) -> User:
        self.users[user_id] = user
        return user

    def delete_user(self, user_id: int) -> Optional[User]:
        return self.users.pop(user_id, None)

    def update_user(self, user_id: int, name: str = None, agency: str = None, account: str = None, current_balance: float = None) -> Optional[User]:
        user = self.users.get(user_id)
        if not user:
            return None

        if name is not None:
            user.name = name
        if agency is not None:
            user.agency = agency
        if account is not None:
            user.account = account
        if current_balance is not None:
            user.current_balance = current_balance

        self.users[user_id] = user
        return user
