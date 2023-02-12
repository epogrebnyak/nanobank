class CurrentAccountsBase:
    def __init__(self):
        self.client_balances = {}
        self.own_account = 0

    def create_user(self, name):
        """Add new a user *name* with zero current account balance."""
        # Is this always a correct thing to do?
        self.client_balances[name] = 0

    def deposit(self, name, amount):
        """Deposit *amount* of cash into current account of *name* user."""
        self.client_balances[name] += amount

    def move(self, from_user, to_user, amount):
        """Move money between user accounts without restrictions or fees."""
        # Should there be any constraints?
        self.client_balances[from_user] -= amount
        self.client_balances[to_user] += amount

    def collect(self, name, amount):
        self.client_balances[name] -= amount
        self.own_account += amount

    @property
    def users(self):
        """List all users with current accounts."""
        # Implement here - you need to list all keys from self.balances dictionary.

    @property
    def all_balances(self):
        return {**self.client_balances, "bank": self.own_account}


class CurrentAccounts(CurrentAccountsBase):
    def add_users(self, names):
        """Write docstring here."""
        # Write code here

    def transfer(self, from_user, to_user, amount, fee=0):
        """Write docstring here."""
        # Write code here using raw_trasfer()


if __name__ == "__main__":
    # Think of alternate constructor for CurrentAccoutns wit user names, and own_account
    accounts = CurrentAccounts()
    accounts.create_user("rajiv")
    accounts.create_user("sara")
    accounts.create_user("jose")
    accounts.deposit("rajiv", 140)
    accounts.deposit("sara", 240)
    accounts.deposit("jose", 30)
    accounts.move("jose", "rajiv", 10)
    accounts.move(from_user="jose", to_user="sara", amount=10)
    print(accounts.client_balances)
