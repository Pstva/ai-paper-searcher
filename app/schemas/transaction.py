import datetime
from enum import Enum

from sqlmodel import SQLModel


class TransactionType(str, Enum):
    deposit = "deposit"
    withdrawal = "withdrawal"


class TransactionStatus(str, Enum):
    pending = "pending"
    succeeded = "succeeded"
    failed = "failed"
    cancelled = "cancelled"


class TransactionCreate(SQLModel):
    transaction_type: TransactionType
    transaction_status: TransactionStatus | None = None


class TransactionRead(SQLModel):
    transaction_type: TransactionType
    transaction_status: TransactionStatus
    created_at: datetime.datetime
    processed_at: datetime.datetime | None


class TransactionUpdate(SQLModel):
    processed_at: datetime.datetime | None = None
    transaction_status: TransactionStatus | None = None
