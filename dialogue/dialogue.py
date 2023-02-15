"""Dialogue system with functions.

Orginal code at:
https://stackoverflow.com/questions/63121722/financial-calculator-bond-interest-woes
"""


def get_text(message):
    return input(message + "\n> ")


def get_number(message):
    return float(get_text(message))


def get_selection(message, options):
    while True:
        answer = get_text(message)
        if answer in options:
            return answer
        else:
            print("Please enter any of:", " ".join(options))


# input
p = get_number("How much are you depositing?")
r = get_number("At which annual interest rate (in percent)?")
t = get_number("How many years are you planning to invest for?")
ans = get_selection("[c]ompound or [f]lat rate?", ["c", "f"])
currency = "R" # this is a money symbol for South African rand https://en.wikipedia.org/wiki/South_African_rand

# all of the calculation logic here in one place
def compound_interest(annual_rate, years):
    return (1 + annual_rate) ** years


def simple_interest(annual_rate, years):
    return 1 + annual_rate * years

# a dictionary can help choosing the right function
interest_func = dict(c=compound_interest, f=simple_interest)[ans]
fv = p * interest_func(annual_rate=r / 100, years=t)

# output
print(
    f"Future value of your initial investment of {currency}{p} "
    + f"over {t} years under {r}% interest rate will be {currency}{fv:.2f}"
)


# IDEA: print the interest rate number to screen (as 2.25%) and ask about correctness 
#       the source of error may be if a user enters 2.25 as 0.0225 
#       (for example thinking a fraction is expected as interest rate)
#       you will need a loop that would iterate if the number is not correct

# IDEA: print("Please enter any of:", " ".join(options)) lists options as a b c
#       you may want to write a, b or c

# IDEA: another option to design a prompt is to suggest options 
#       enter c for compund rate, f for flat rate. your expected 
#       option parameter would need to change to a dicitonary. 

# MORE: add dates (today and in the future), suggest a contract with lower or higher interest rate
#       use a floating interest rate depending on inflation of central bank prime rate,
#       save data to file, create an API for this deposit product, think of incentive 
#       schemes for deposit providers and rebate a deposit provider with a small cashback.
#       print some ASCII art - for example Decimal Dan from banner.txt 
#       (generated form http://gordlaws.co.za/gcs-decimal-dan/ using https://www.ascii-art-generator.org/)
