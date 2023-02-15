"""Dialogue system with functions.

Orginal code at:
https://stackoverflow.com/questions/63121722/financial-calculator-bond-interest-woes
"""


def compound_interest(annual_rate, years):
    return (1 + annual_rate) ** years


def simple_interest(annual_rate, years):
    return 1 + annual_rate * years


def get_text(message):
    return input(message + "\n> ")


def get_number(message):
    return float(get_text(message))


def get_selection(message, options):
    while True:
        ans = get_text(message)
        if ans in options:
            return ans
        else:
            print("Please enter any of:", " ".join(options))


# input
p = get_number("How much are you depositing?")
r = get_number("At which annual interest rate (in percent)?")
t = get_number("How many years are you planning to invest for?")
ans = get_selection("[c]ompound or [f]lat rate?", ["c", "f"])

# all of the calculation logic here in one place
interest_func = dict(c=compound_interest, f=simple_interest)[ans]
fv = p * interest_func(annual_rate=r / 100, years=t)
# output
currency = "R"
print(
    f"Future value of your initial investment of {currency}{p} "
    + f"over {t} years under {r}% interest rate will be {currency}{fv:.2f}"
)
