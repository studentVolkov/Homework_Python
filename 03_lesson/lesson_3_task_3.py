from address import Address
from mailing import Mailing

to_address = Address
from_address = Address
to_address = 592308, "г. Tomsk", "ул.Добрая", 2, 33
from_address = 324567, "г. Елань", "ул. Петрова", 12, 11

sending = Mailing
sending(to_address, from_address, 2121, 1234567890)

print(
    "Отправление",
    sending.track,
    "из",
    from_address,
    "в",
    to_address,
    ". Стоимость",
    sending.cost,
    "рублей.",
)
