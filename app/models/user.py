from typing import TYPE_CHECKING

from .utils import (
    PASSWORD_RULES,
    USER_NAME_RULES,
    is_strong_password,
    is_valid_email,
    is_valid_user_name,
    make_password_hash,
)

if TYPE_CHECKING:
    from .user_balance import UserBalance


class User:
    """Represents a user in the system."""

    def __init__(self, id: str, name: str, password: str, email: str) -> None:
        """Init an instance of the class User

        Args:
            id (str): the unique identificator of the user
            name (str): the user name
            password (str): the user password
            email (str): the email of the user
        """
        self.id = id
        self.name = name
        self.email = email

        self.__validate_name()
        self.__validate_email()
        self.__validate_password(password=password)
        self.__add_password_hash(password=password)

        self.balance = UserBalance(user=self)

    def __validate_name(self) -> None:
        """Validate user name.

        Args:
            name (str): name of the user

        Raises:
            ValueError: if the user name is not valid.
        """
        if not is_valid_user_name(user_name=self.name):
            raise ValueError(f"{USER_NAME_RULES}")

    def __validate_password(self, password: str) -> None:
        """Validate password complexity.

        Args:
            password (str): Password string to validate.

        Raises:
            ValueError: if the password is not valid.
        """
        if not is_strong_password(password=password):
            raise ValueError(PASSWORD_RULES)

    def __validate_email(self) -> None:
        """Validate email.

        Args:
            email (str): email of the user

        Raises:
            ValueError: if the email is not valid.
        """
        if not is_valid_email(email=self.email):
            raise ValueError("Not valid email.")

    def __add_password_hash(self, password: str) -> None:
        """Add the password hash to the properties.

        Args:
            password (str): password provided by the user
        """
        self.password_hash = make_password_hash(password=password)

    # TODO !!!!
    def make_request(self):
        pass

    def top_up_balance(self, n: int):
        self.balance.add(n)


class Admin(User):
    def __init__(self, id: str, name: str, password: str, email: str) -> None:
        """Init admin user.

        Args:
            id (str): the unique identificator of the user
            name (str): the user name
            password (str): the user password
            email (str): the email of the user
        """
        super().__init__(id=id, name=name, password=password, email=email)
        self.__is_admin = True

    @property
    def is_admin(self):
        return self.__is_admin

    @classmethod
    def make_new_user(
        id: str,
        name: str,
        password: str,
        email: str,
        is_admin: bool = False,
    ) -> User:
        """Add new user by admin.

        Args:
            id (str): the unique identificator of the user
            name (str): the user name
            password (str): the user password
            email (str): the email of the user
            is_admin (bool, optional): is the user should be an admin user.
                Defaults to False.

        Returns:
            User: instance of the User class
        """
        if not is_admin:
            return User(id=id, name=name, password=password, email=email)
        return Admin(id=id, name=name, password=password, email=email)

    # I will add other admin-specific methods later


if __name__ == "__main__":
    user = User(id=1, name="Alena", password="Abcdef1!", email="alpest@mail.ru")
    print("user")
    print("id: ", user.id)
    print("name: ", user.name)
    print("password hash: ", user.password_hash)
    print("email: ", user.email)
    print()

    print()
    admin = Admin(
        id="2", name="AlenaAdmin", password="Abcdef1!_", email="myadmin@yandex.com"
    )
    print("id", admin.id)
    print("name: ", admin.name)
    print("password hash: ", admin.password_hash)
    print("email: ", admin.email)
