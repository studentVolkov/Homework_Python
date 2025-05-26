from smartphone import Smartphone

phone1 = Smartphone("Haier", "op902", "+79234002929")
phone2 = Smartphone("Huawei", "lp99", "+79523469067")
phone3 = Smartphone("Apple", "gold", "+79990000000")
phone4 = Smartphone("Garmoshka", "zzz", "+79123332324")
phone5 = Smartphone("Samsung", "D500", "+79132342566")

catalog = [phone1, phone2, phone3, phone4, phone5]


def print_phone(phone: Smartphone):
    print(f"{phone.brand} - {phone.model}. {phone.number}")


for phone in catalog:
    print_phone(phone)
