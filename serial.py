# %%
balances = dict(bank=0)
print(balances)

# initial deposits
balances["rajiv"] = 50
print(balances)
balances["sara"] = 140
print(balances)
balances["jose"] = 20.5
print(balances)

# transfer 10 from jose to rajiv
balances["jose"] = balances["jose"] - 10
balances["rajiv"] = balances["rajiv"] + 10
print(balances)

# transfer 10 from jose to sara
balances["jose"] -= 10
balances["sara"] += 10
print(balances)

# transfer 5 from jose to bank and close account
balances["jose"] -= 0.5
balances["bank"] += 0.5
del balances["jose"]
print(balances)


# %%
def transfer(balances, from_user, to_user, amount):
    balances[from_user] = balances[from_user] - amount
    balances[to_user] = balances[to_user] + amount
    return balances


def create_balances():
    return dict(bank=0)


def topup(balances, name, amount):
    """Deposit money into *name_to* account in cash or from other bank."""
    balances[name] = balances[name] + amount
    return balances


def add_user(balances, name, amount=0):
    balances[name] = amount
    return balances


balances = create_balances()
balances = add_user(balances, "rajiv")
balances = topup(balances, "rajiv", 140)
balances = add_user(balances, "sara", 240)
balances = add_user(balances, "jose", amount=30)
balances = transfer(balances, "jose", "rajiv", 10)
balances = transfer(balances, "jose", "sara", 10)
print(balances)
assert balances == {"bank": 0, "rajiv": 150, "sara": 250, "jose": 10}


class Accounts:
    def __init__(self):
        self.balances = {"bank": 0}

    def add_user(self, name):
        self.balances[name] = 0

    def add_users(self, names):
        pass

    def topup(self, name, amount):
        """Deposit money into *name_to* account in cash or from other bank."""
        self.balances[name] = self.balances[name] + amount

    def raw_transfer(self, from_user, to_user, amount):
        """Transfer money into *name_to* account in cash or from other bank."""
        self.balances[from_user] = self.balances[from_user] - amount
        self.balances[to_user] = self.balances[to_user] + amount

    def transfer(self, from_user, to_user, amount):
        """Write docstring here."""
        pass

    def transfer_with_fee(self, from_user, to_user, amount, fee):
        """Write docstring here."""
        pass


accounts = Accounts()
accounts.add_user("rajiv")
accounts.add_user("sara")
accounts.add_user("jose")
accounts.topup("rajiv", 140)
accounts.topup("sara", 240)
accounts.topup("jose", 30)
accounts.raw_transfer("jose", "rajiv", 10)
accounts.raw_transfer(from_user="jose", to_user="sara", amount=10)
print(accounts.balances)

from pydantic import BaseModel
from typing import Literal


class PaymentEvent(BaseModel):
    pass


class AddUser(PaymentEvent):
    operation: Literal["add_user"] = "add_user"
    name: str


class DeleteUser(PaymentEvent):
    operation: Literal["delete_user"] = "delete_user"
    name: str


class Topup(PaymentEvent):
    operation: Literal["topup"] = "topup"
    user: str
    amount: int


class RawTransfer(PaymentEvent):
    operation: Literal["raw_transfer"] = "raw_transfer"
    from_user: str
    to_user: str
    amount: int


event_objects = [
    AddUser(name="rajiv"),
    AddUser(name="sara"),
    AddUser(name="jose"),
    Topup(user="rajiv", amount=240),
    Topup(user="sara", amount=140),
    Topup(user="jose", amount=30),
    RawTransfer(from_user="jose", to_user="rajiv", amount=10),
    RawTransfer(from_user="jose", to_user="sara", amount=10),
    DeleteUser(name="jose"),
]


def process_event(accounts, event):
    if isinstance(event, AddUser):
        accounts.add_user(event.name)
    elif isinstance(event, Topup):
        accounts.topup(event.user, event.amount)
    elif isinstance(event, RawTransfer):
        accounts.raw_transfer(event.from_user, event.to_user, event.amount)
    return accounts


more_accounts = Accounts()
for event in event_objects:
    more_accounts = process_event(more_accounts, event)
print(more_accounts.balances)

from pydantic import BaseModel
from typing import List


class Events(BaseModel):
    events: List[PaymentEvent]


es = Events(events=event_objects).dict()
print(es)

assert es == {
    "events": [
        {"operation": "add_user", "name": "rajiv"},
        {"operation": "add_user", "name": "sara"},
        {"operation": "add_user", "name": "jose"},
        {"operation": "topup", "user": "rajiv", "amount": 240},
        {"operation": "topup", "user": "sara", "amount": 140},
        {"operation": "topup", "user": "jose", "amount": 30},
        {
            "operation": "raw_transfer",
            "to_user": "rajiv",
            "from_user": "jose",
            "amount": 10,
        },
        {
            "operation": "raw_transfer",
            "to_user": "sara",
            "from_user": "jose",
            "amount": 10,
        },
        {"operation": "delete_user", "name": "jose"},
    ]
}
