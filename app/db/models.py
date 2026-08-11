from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Text


class Base(DeclarativeBase):
    pass


class UserMemory(Base):
    __tablename__ = "user_memories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(index=True)
    key: Mapped[str] = mapped_column(String(100))
    value: Mapped[str] = mapped_column(Text)


class SudoUser(Base):
    __tablename__ = "sudo_users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(index=True, unique=True)

    ai: Mapped[bool] = mapped_column(default=True)
    groups: Mapped[bool] = mapped_column(default=False)
    broadcast: Mapped[bool] = mapped_column(default=False)
    logs: Mapped[bool] = mapped_column(default=False)
    voice: Mapped[bool] = mapped_column(default=False)
    maintenance: Mapped[bool] = mapped_column(default=False)
    config: Mapped[bool] = mapped_column(default=False)
