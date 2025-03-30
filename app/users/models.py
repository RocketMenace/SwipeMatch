from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Date, DateTime, ForeignKey
from datetime import date, datetime, timezone

from app.config.database import database


class User(database.Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(
        primary_key=True, index=True, autoincrement=True, nullable=False
    )
    email: Mapped[str] = mapped_column(String(length=50), nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(String(length=50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(length=50), nullable=False)
    city: Mapped[str] = mapped_column(String(length=50), nullable=False)
    interests: Mapped[list["Interests"]] = relationship(back_populates="user")
    preferences: Mapped["Preferences"] = relationship(
        back_populates="user", uselist=False, cascade="all, delete-orphan"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), default=datetime.now(tz=timezone.utc)
    )
    birthday: Mapped[date] = mapped_column(Date(), nullable=False)

    def __repr__(self):
        return f"{self.first_name} {self.last_name} {self.email}"


class Interests(database.Base):
    __tablename__ = "interests"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=50), nullable=False)

    def __repr__(self):
        return f"{self.id} {self.name}"


class Preferences(database.Base):
    __tablename__ = "preferences"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    user: Mapped["User"] = relationship(back_populates="preferences")
    sex: Mapped[str] = mapped_column(String(length=50), nullable=False)
    age_from: Mapped[int] = mapped_column(Integer)
    age_to: Mapped[int] = mapped_column(Integer)

    def __repr__(self):
        return f"{self.id} {self.sex}"
