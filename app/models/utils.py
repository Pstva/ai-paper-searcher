import random
import re
from hashlib import pbkdf2_hmac

PASSWORD_RULES = """
The password should meet the following rules:
- Minimum length: 8 characters
- Contains at least one lowercase letter (a-z)
- Contains at least one uppercase letter (A-Z)
- Contains at least one digit (0-9)
- Contains at least one special character (a character that is not a letter, digit,
    underscore or whitespace)
"""

EMAIL_RULES = """
The email address should conform to a common,
pragmatic subset of RFC-style addresses. Rules enforced by the regular
expression:
    - Local part contains one or more characters from [A-Za-z0-9._%+-]
    - Exactly one "@" separator
    - Domain part is composed of labels separated by dots; each label contains
    letters, digits or hyphens (no leading/trailing dot)
    - Top-level domain (final label) is at least 2 ASCII letters
"""

USER_NAME_RULES = """
The user name should not be less than 3 characters and should be more then 20 characters.
"""


def is_strong_password(password: str) -> bool:
    f"""Validate password complexity.

    {PASSWORD_RULES}

    Args:
        password (str): Password string to validate.

    Returns:
        bool: True if the password satisfies all complexity requirements, False otherwise.

    Examples:
        >>> is_strong_password("Abcdef1!")
        True
        >>> is_strong_password("password")
        False
        >>> is_strong_password("Short1!")
        False
    """
    if not password or not isinstance(password, str):
        return False
    pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s]).{8,}$")
    return (bool(pattern.fullmatch(password)),)


def is_valid_email(email: str) -> bool:
    f"""
    Validate a simple, practical email address format.

    {EMAIL_RULES}

    Args:
        address (str): Email address to validate.

    Returns:
        bool: True if the address matches the pattern, False otherwise.

    Examples:
        >>> is_valid_email("user@example.com")
        True
        >>> is_valid_email("user.name+tag@sub.domain.co")
        True
        >>> is_valid_email("invalid@localhost")
        False
        >>> is_valid_email("a\"b(c)d,e:f;<>[]@example.com")
        False
    """
    email_pattern = re.compile(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}$"
    )
    email = email.strip()
    if not email or not isinstance(email, str):
        return False
    return bool(email_pattern.fullmatch(email))


def is_valid_user_name(user_name: str) -> bool:
    f"""Validate user name.

    {USER_NAME_RULES}

    Args:
        name (str): name of the user

    Returns:
        bool: True if the name satsfies all requirements, False otherwise.
    """
    MIN_LEN, MAX_LEN = 3, 20
    if len(user_name) < MIN_LEN or len(user_name) > MAX_LEN:
        return False
    return True


def make_password_hash(password: str) -> str:
    """Makes the hash of the password.

    Args:
        password (str): password provided by the user

    Returns:
        str: hash of the password
    """
    iters = random.randint(a=100000, b=200000)
    salt = random.randbytes(n=10) * 2
    dk = pbkdf2_hmac("sha256", bytes(password, encoding="utf-8"), salt, iters)
    return dk.hex()
