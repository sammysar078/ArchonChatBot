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
