from faker import Faker

fake = Faker('ru_RU')

user_data = {
    "name": fake.name(),
    "address": fake.address(),
    "email": fake.email()
}
print(fake.name())
print(fake.address())
print(fake.email())