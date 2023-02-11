from with_class import CurrentAccounts

accounts = CurrentAccounts()

from faker import Faker
from random import randint 

def fake_account():
    fake = Faker("id_ID")
    name = fake.first_name()
    name=name[:min(4, len(name))]
    amount = randint(5, 75)
    return name, amount       

fake_account()

from fastapi import FastAPI
app = FastAPI()



@app.get("/seed/{n}")
def random(n: int):
    for _ in range(n):
        name, amount = fake_account()
        accounts.create_user(name)
        accounts.add_money(name, amount)    

@app.get("/users")
def show():
    return accounts.client_balances

@app.get("/")
def show_all():
    return {**accounts.client_balances, **{"bank": accounts.own_account}}

@app.get("/create")
def create_user(user: str):
    accounts.create_user(user)
    return dict(user=user)

@app.get("/user/{name}")
def get_balance(name: str):
    return dict(user=name, balance=accounts.client_balances[name])

@app.get("/user/{name}/topup")
def topup(name: str, amount: float):
    accounts.add_money(name, amount)
    return dict(user=amount, added=amount)

@app.get("/user/{name}/transfer")
def transfer(name: str, to: str, amount: float):
    kwarg = dict(from_user=name, to_user=to, amount=amount)
    accounts.raw_transfer(**kwarg)
    return kwarg