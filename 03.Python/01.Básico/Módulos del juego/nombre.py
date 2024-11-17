from faker import Faker

def generar_nombre():
    fake = Faker()
    return fake.name()