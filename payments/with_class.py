class CurrentAccountsBase:

    def __init__(self):
        self.client_balances = {}
        self.own_account = 0

    @property    
    def users(self):
        """List all users with current accounts."""
        # Implement here - you need to list all keys from self.balances dictionary.

    @property
    def all_balances(self):
        return {**self.client_balances, "bank": self.own_account}

    def create_user(self, name):
        """Add new a user *name* with zero current account balance."""
        # Is this always a correct thing to do?
        self.client_balances[name] = 0

    def add_money(self, name, amount):
        """Deposit *amount* of cash into current account of *name* user."""
        self.client_balances[name] = self.client_balances[name] + amount

    def raw_transfer(self, from_user, to_user, amount):
        """Transfer money between user accounts."""
        # Should there be any constraints? (There are at least 2 to 4 constraints to consider).
        self.client_balances[from_user] = self.client_balances[from_user] - amount
        self.client_balances[to_user] = self.client_balances[to_user] + amount
       

class CurrentAccounts(CurrentAccountsBase):
    def add_users(self, names):
        """Write docstring here."""
        # Write code here

    def transfer(self, from_user, to_user, amount):
        """Write docstring here."""
        # Write code here using raw_trasfer()

    def collect_fee(self, from_user, amount):
        """Write off *amount* from a user and send money to bank own account."""
        # Write code here usig trasfer and collect_fees()

    def transfer_with_fee(self, from_user, to_user, amount, fee):
        """Write docstring here."""
        # Write code here

if __name__ == "__main__":
    # Think of alternate constructor for CurrentAccoutns wit user names, and own_account
    accounts = CurrentAccounts()
    accounts.create_user("rajiv")
    accounts.create_user("sara")
    accounts.create_user("jose")
    accounts.add_money("rajiv", 140)
    accounts.add_money("sara", 240)
    accounts.add_money("jose", 30)
    accounts.raw_transfer("jose", "rajiv", 10)
    accounts.raw_transfer(from_user="jose", to_user="sara", amount=10)
    print(accounts.client_balances)
