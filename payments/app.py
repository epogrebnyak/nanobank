from fastapi import FastAPI
from pydantic import BaseModel
from decimal import Decimal
from typing import Dict, Union

app = FastAPI()


class Fee(BaseModel):
    flat: Union[float, int]
    rate: float

    def calculate(self, amount):
        _x = Decimal(self.flat) + Decimal(self.rate) * Decimal(amount)
        return round(_x, 2)


class CurrentAccounts(BaseModel):
    client_balances: Dict[str, Decimal]
    own_account: Decimal = Decimal(0)
    fee: Fee = Fee(flat=0, rate=0)
    currency: str = ""

    @property
    def users(self):
        """List all users."""
        return list(self.client_balances.keys())

    def create_user(self, name, amount=0):
        """Add new a user *name* with *amount* current account balance."""
        if name not in self.users:
            self.client_balances[name] = Decimal(0)
            if amount:
                self.deposit(name, amount)
            return True
        return False

    def deposit(self, name, amount):
        """Deposit *amount* of cash into current account of *name* user."""
        self.client_balances[name] += Decimal(amount)
        return True

    def move(self, from_user, to_user, amount):
        """Move money between user accounts without restrictions or fees."""
        self.client_balances[from_user] -= Decimal(amount)
        self.client_balances[to_user] += Decimal(amount)
        return True

    def collect(self, name, amount):
        """Collect fee from user account to bank account."""
        self.client_balances[name] -= amount
        self.own_account += amount
        return True

    def transfer(self, from_user, to_user, amount):
        """Transfer money between user accounts."""
        if amount <= self.client_balances[from_user]:
            self.move(from_user, to_user, amount)
            fee = self.fee.calculate(amount)
            if fee:
                self.collect(from_user, fee)
            return True
        else:
            return False


accounts = CurrentAccounts(client_balances={}, fee=Fee(flat=0.25, rate=0.005))

import faker
from random import randint


def fake_name(locale="id_ID"):
    fake = faker.Faker(locale)
    return fake.first_name()[:5].lower()


def fake_amount(a=1, b=50):
    return Decimal(round(randint(a * 100, b * 100) / 100 + 0.01, 2))


@app.get("/create/users/random")
def random(n: int = 5, locale="id_ID"):
    pairs = [(fake_name(locale), fake_amount()) for _ in range(n)]
    for name, amount in pairs:
        accounts.create_user(name)
        accounts.deposit(name, amount)
    return {"n": n, "locale": locale, "seed": pairs}


@app.get("/")
def start():
    return "Refer to /docs for help with this API."


@app.get("/users")
def users():
    return accounts.users


@app.get("/bank")
def bank():
    return {"_bank": accounts.own_account}


@app.get("/balances")
def balances():
    return {**bank(), **accounts.client_balances}


@app.get("/create/user")
def create_user(name: str, amount=0):
    flag = accounts.create_user(name, amount)
    return dict(is_created=flag, user=name, deposit=amount)


@app.get("/user/{name}")
def get_balance(name: str):
    return dict(user=name, balance=accounts.client_balances[name])


@app.get("/user/{name}/deposit")
def deposit(name: str, amount: float):
    flag = accounts.deposit(name, amount)
    return dict(is_finished=flag, user=amount, amount_added=amount)


@app.get("/user/{name}/transfer")
def transfer(name: str, to: str, amount: Decimal):
    kwarg = dict(from_user=name, to_user=to, amount=amount)
    flag = accounts.transfer(**kwarg)
    return {"is_executed": flag, "args": kwarg}


@app.get("/fee")
def fee(amount):
    return {"amount": amount, "fee": accounts.fee.calculate(amount)}
