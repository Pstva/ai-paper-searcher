from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User


class UserBalance:
    def __init__(self, user: User):
        self.user = user
        self.__balance = 0

    @property
    def get_balance(self):
        return self.__balance

    def add(self, n: int):
        assert n >= 0, "You can only add a non-negative number to the balance."
        self.__balance += n

    def debit(self, n: int):
        assert n >= 0, "You can only debit a non-negative number from the balance."
        self.__balance -= n
