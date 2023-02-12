from faker import Faker
from random import randint


def fake_name(locale="id_ID"):
    fake = Faker(locale)
    _name = fake.first_name()
    n = min(5, len(_name))
    return _name[:5].lower()


def fake_amount(a, b):
    return round(randint(a * 100, b * 100) / 100 + 0.01, 2)


if __name__ == "__main__":
    for _ in range(10):
        x = fake_name(), fake_amount(5, 75)
        print(x)
