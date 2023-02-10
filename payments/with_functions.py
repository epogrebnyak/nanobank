def create_balances():
    return dict(bank=0)


def add_user(balances, name, amount=0):
    balances[name] = amount
    return balances


def deposit_cash(balances, name, amount):
    """Deposit money into *name_to* account in cash or from other bank."""
    balances[name] = balances[name] + amount
    return balances


def transfer(balances, from_user, to_user, amount):
    balances[from_user] = balances[from_user] - amount
    balances[to_user] = balances[to_user] + amount
    return balances


# Creating a dictionary
balances = create_balances()

#  Creating users and balances
balances = add_user(balances, "rajiv")
balances = deposit_cash(balances, "rajiv", 40)
balances = add_user(balances, "sara", 140)
balances = add_user(balances, "jose", 30)

# Making two money transfers
balances = transfer(balances, "jose", "rajiv", 10)
balances = transfer(balances, "jose", "sara", 10)
print(balances)

# A test for our code
assert balances == {"bank": 0, "rajiv": 50, "sara": 150, "jose": 10}
