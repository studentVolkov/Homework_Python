def is_year_leap(year) -> bool:
    return year % 4 == 0


year = 2024
is_leap = is_year_leap(year)
print(f'год {year}: {is_leap}')
