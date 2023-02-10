class Accounts:
    def __init__(self):
        self.balances = {"bank": 0}

    def add_user(self, name):
        # is this always correct to do?
        self.balances[name] = 0

    def deposit_cash(self, name, amount):
        """Deposit *amount* of cash into *name* account."""
        self.balances[name] = self.balances[name] + amount

    def raw_transfer(self, from_user, to_user, amount):
        """Transfer money between users."""
        self.balances[from_user] = self.balances[from_user] - amount
        self.balances[to_user] = self.balances[to_user] + amount

    def transfer(self, from_user, to_user, amount):
        """Write docstring here."""
        pass

    def transfer_with_fee(self, from_user, to_user, amount, fee):
        """Write docstring here."""
        pass

    def add_users(self, names):
        """Write docstring here."""
        pass


accounts = Accounts()
accounts.add_user("rajiv")
accounts.add_user("sara")
accounts.add_user("jose")
accounts.deposit_cash("rajiv", 140)
accounts.deposit_cash("sara", 240)
accounts.deposit_cash("jose", 30)
accounts.raw_transfer("jose", "rajiv", 10)
accounts.raw_transfer(from_user="jose", to_user="sara", amount=10)
print(accounts.balances)
