"""Handles database connection and tables"""
from sqlalchemy.engine.base import Engine
from sqlalchemy import (
    Column,
    String,
    create_engine,
)
from sqlalchemy.orm import declarative_base
import user_service.settings as Config

# Database Configuration
DB_ENGINE: Engine = create_engine(Config.DATABASE_URL)
BASE = declarative_base()


# Define SQLAlchemy Models
class User(BASE):  # type: ignore # pylint: disable=too-few-public-methods
    """User model"""

    __tablename__ = "User"
    id: Column = Column(String, primary_key=True)
    firstName: Column = Column(String)
    lastName: Column = Column(String)
    phoneNumber: Column = Column(String)


if __name__ == "__main__":
    BASE.metadata.drop_all(DB_ENGINE)
    BASE.metadata.create_all(DB_ENGINE)
