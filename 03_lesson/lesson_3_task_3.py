from address import Address
from mailing import Mailing

to_address = Address(592308, "г. Томск", "ул.Добрая", 2, 33)
from_address = Address(324567, "г. Елань", "ул. Петрова", 12, 11)

sending = Mailing(to_address, from_address, 2121, 1234567890)

print(f"Отправление {sending.track} из {sending.from_address} в "
      "{sending.to_address}. Стоимость {sending.cost} рублей.")
