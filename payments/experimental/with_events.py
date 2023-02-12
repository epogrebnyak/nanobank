# print(28.60 - 14.20 - 14.20)
# 0.20000000000000284

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


class DepositCash(PaymentEvent):
    operation: Literal["deposit_cash"] = "deposit_cash"
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
    DepositCash(user="rajiv", amount=240),
    DepositCash(user="sara", amount=140),
    DepositCash(user="jose", amount=30),
    RawTransfer(from_user="jose", to_user="rajiv", amount=10),
    RawTransfer(from_user="jose", to_user="sara", amount=10),
    DeleteUser(name="jose"),
]


def process_event(accounts, event):
    if isinstance(event, AddUser):
        accounts.add_user(event.name)
    elif isinstance(event, DepositCash):
        accounts.deposit_cash(event.user, event.amount)
    elif isinstance(event, RawTransfer):
        accounts.raw_transfer(event.from_user, event.to_user, event.amount)
    # are we missing anything?
    return accounts


from with_class import Accounts

accounts = Accounts()
for event in event_objects:
    print("Processing", event)
    accounts = process_event(accounts, event)
print(accounts.balances)

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
        {"operation": "deposit_cash", "user": "rajiv", "amount": 240},
        {"operation": "deposit_cash", "user": "sara", "amount": 140},
        {"operation": "deposit_cash", "user": "jose", "amount": 30},
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
