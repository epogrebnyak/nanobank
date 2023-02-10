# works at https://timeweb.cloud/my/database/20343
# Run before script:
#  pip install SQLAlchemy sqlalchemy-utils mysql-connector-python==8.0.32 mysqlclient==2.1.1

url = "mysql://gen_user:1l211wm8g3@81.200.144.2:3306/default_db"

from sqlalchemy import create_engine

engine = create_engine(url, echo=True)
with engine.connect() as connection:
    pass

from sqlalchemy_utils import database_exists

print(database_exists(engine.url))

from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine
from decimal import Decimal


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    family_name: str
    given_name: str


class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    holder_id: Optional[int] = Field(default=None, foreign_key="person.id")
    balance: Decimal
    currency: str


hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
