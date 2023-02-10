from faker import Faker

fake = Faker("en_IN")
for _ in range(10):
    print(fake.bank())

for _ in range(20):
    print(fake.first_name(), fake.last_name())
