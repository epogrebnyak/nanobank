def create_balances():
    """Write docstring here."""
    return dict(bank=0)


def create_user(balances, name, amount=0):
    """Write docstring here."""
    balances[name] = amount
    return balances


def add_money(balances, name, amount):
    """Deposit money into *name_to* account in cash or from other bank."""
    balances[name] = balances[name] + amount
    return balances


def transfer(balances, from_user, to_user, amount):
    """Write docstring here."""
    # Is this always correct?
    balances[from_user] = balances[from_user] - amount
    balances[to_user] = balances[to_user] + amount
    return balances


# Creating a dictionary
balances = create_balances()

#  Creating users and balances
balances = create_user(balances, "rajiv")
balances = add_money(balances, "rajiv", 40)
balances = create_user(balances, "sara", 140)
balances = create_user(balances, "jose", 30)

# Making two money transfers
balances = transfer(balances, "jose", "rajiv", 10)
balances = transfer(balances, "jose", "sara", 10)
print(balances)

# A test for our code
assert balances == {"bank": 0, "rajiv": 50, "sara": 150, "jose": 10}

# Problems:
# 1. Overspending
print(transfer(balances, "jose", "sara", 199))

# 2. Not earning money
print(balances["bank"])

# 3. Cannot save the state of the accounts and read back

# 4. Cannot prove correctness - no tests

# 5. There are situations where the program will crash or misbehave.