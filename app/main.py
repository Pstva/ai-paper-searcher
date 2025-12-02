import os
from typing import List, Optional

from models.chat_request import ChatCompletionRequest
from models.chat_response import ChatResponse
from models.transaction import Transaction
from models.user import User
from services.user import (
    create_user,
    delete_user,
    get_all_users,
    get_user_by_email,
    get_user_by_id,
)
from sqlmodel import Session, SQLModel, create_engine

test_file = "test.db"
if os.path.exists(test_file):
    os.remove(test_file)
engine = create_engine(f"sqlite:///./{test_file}", echo=False)
SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    test_user1 = User(
        id=1,
        name="Bla Bla",
        password_hash="Abcdef1!@3",
        email="alpest@mail.ru",
        balance=10,
        user_type="user",
    )
    test_user2 = User(
        name="Bla Bla2",
        password_hash="Abcdef1!@35",
        email="alpest2@mail.ru",
        user_type="user",
    )
    test_user3 = User(
        name="AdminUser",
        password_hash="Abcdef1!@305",
        email="admin@mail.ru",
        user_type="admin",
    )
    with Session(engine) as session:

        create_user(test_user1, session)
        create_user(test_user2, session)
        create_user(test_user3, session)

        users = get_all_users(session)
        for user in users:
            print(user)

        user0 = get_user_by_email(email="alpest@mail.ru", session=session)
        print(user0)
        user1 = get_user_by_id(user_id=2, session=session)
        print(user1)
        u_id = 3
        print(f"Deleted user {u_id}: {delete_user(user_id=u_id, session=session)}")
        print(users)

        users = get_all_users(session)
        for user in users:
            print(user)
