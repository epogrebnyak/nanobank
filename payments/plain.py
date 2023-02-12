"""Dictionary as a simple data structre for a payment system."""

# `balances`` is a dictionary that holds name-amount pairs.
balances = dict(bank=0.0)
print("1. Empty bank, no customers, just own bank account")
print(balances)

# make initial cash deposits into accounts
print("\n2. Opening accounts for three persons...")
balances["rajiv"] = 50
print(balances)
balances["sara"] = 140
print(balances)
balances["jose"] = 20.5
print(balances)

# transfer 10 from jose to rajiv
print("\n3. Transfering money from `jose` to `rajiv`...")
balances["jose"] = balances["jose"] - 10
balances["rajiv"] = balances["rajiv"] + 10
print(balances)

# transfer 10 from jose to sara
print("\n4. Transfering money from `jose` to `sara`...")
balances["jose"] -= 10
balances["sara"] += 10
print(balances)

# transfer 5 from jose to bank and close account
print("\n5. Transfering small amount to a bank and closing account...")
balances["jose"] -= 0.5
balances["bank"] += 0.5
del balances["jose"]
print(balances)
