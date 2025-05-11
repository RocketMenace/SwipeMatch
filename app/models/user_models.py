from datetime import date, datetime, timezone

from sqlalchemy import (Column, Date, DateTime, ForeignKey, Integer, String,
                        Table)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database import database

# class UserInterest(database.Base):
#     """Association table for users and interests."""
#
#     __tablename__ = "user_interests"
#     id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
#     user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
#     interest_id: Mapped[int] = mapped_column(
#         ForeignKey("interests.id"), primary_key=True
#     )
#     # user: Mapped["User"] = relationship(back_populates="user_interests")
#     # interest: Mapped["Interest"] = relationship(back_populates="interests_user")

user_interest = Table(
    "user_interest",
    database.Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("interest_id", Integer, ForeignKey("interests.id")),
)


class User(database.Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(
        primary_key=True, index=True, autoincrement=True, nullable=False
    )
    email: Mapped[str] = mapped_column(String(length=50), nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(String(length=50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(length=50), nullable=False)
    city: Mapped[str] = mapped_column(String(length=50), nullable=False)
    interest: Mapped[list["Interest"]] = relationship(
        back_populates="user", secondary=user_interest
    )
    preferences: Mapped["Preferences"] = relationship(
        back_populates="user", uselist=False, cascade="all, delete-orphan"
    )
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now())
    birthdate: Mapped[date] = mapped_column(Date(), nullable=False)
    password: Mapped[str] = mapped_column(String(length=50), nullable=False)

    def __repr__(self):
        return f"{self.first_name} {self.last_name} {self.email}"


class Interest(database.Base):
    __tablename__ = "interests"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=50), nullable=False, unique=True)
    user: Mapped[list["User"]] = relationship(
        back_populates="interest", secondary=user_interest
    )

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
