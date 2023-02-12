"""Start server before this script:

  poetry run uvicorn payments.app:app --reload 

In another terminal run this script.  

"""

commands = """
/create/users/random?n=3
/create/user?name=pavel&amount=600.5
/create/user?name=olga
/user/olga/deposit?amount=800
/balances
/user/pavel/transfer?to=olga&amount=500
/user/olga/transfer?to=pavel&amount=525
/user/pavel
/user/olga
/balances

/fee?amount=100
"""

import requests
from pprint import pprint

base_url = "http://127.0.0.1:8000"
lines = [line for line in commands.split() if line and not line.startswith("#")]
for line in lines:
    url = base_url + line
    print("\nQuery:", url)
    data = requests.get(url).json()
    print("Response:")
    pprint(data)

# Excercises:
# - What happens if you run this code again? Are there new users? Why are they being added?
# - Start an account in your name and deposit some money.
# - Start another account in your name and deposit some money.
# - Move all money to one account. Beware of the fees.
# - What parts of this API are realistic and what not. Explain why.
