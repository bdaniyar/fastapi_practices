from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.base import Base


class User(Base):
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

