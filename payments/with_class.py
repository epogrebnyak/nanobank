class Accounts:
    def __init__(self):
        self.balances = {"bank": 0}

    def create_user(self, name):
        # Is this always correct to do?
        self.balances[name] = 0

    def add_money(self, name, amount):
        """Deposit *amount* of cash into *name* account."""
        self.balances[name] = self.balances[name] + amount

    def raw_transfer(self, from_user, to_user, amount):
        """Transfer money between users."""
        # Are there any constraints?
        self.balances[from_user] = self.balances[from_user] - amount
        self.balances[to_user] = self.balances[to_user] + amount

    def transfer(self, from_user, to_user, amount):
        """Write docstring here."""
        # Write code here

    def transfer_with_fee(self, from_user, to_user, amount, fee):
        """Write docstring here."""
        # Write code here

    def add_users(self, names):
        """Write docstring here."""
        # Write code here


accounts = Accounts()
accounts.create_user("rajiv")
accounts.create_user("sara")
accounts.create_user("jose")
accounts.add_money("rajiv", 140)
accounts.add_money("sara", 240)
accounts.add_money("jose", 30)
accounts.raw_transfer("jose", "rajiv", 10)
accounts.raw_transfer(from_user="jose", to_user="sara", amount=10)
print(accounts.balances)

# API: 
"user/create", ("rajiv")
"account/topup", ("rajiv", 140)
"account/transfer", ("jose", "sara", 10, 0.5)
"accounts/"