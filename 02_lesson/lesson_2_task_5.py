seasons = {
    "зима": [12, 1, 2],
    "весна": [3, 4, 5],
    "лето": [6, 7, 8],
    "осень": [9, 10, 11]
}


def month_to_season(n):
    """
    Возвращает по индексу месяца
    имя сезона, задекларированное в seasons
    """
    # Перебрать словарь seasons по элементам, где season_name - ключ,
    # month_indexes - значение
    for season_name, month_indexes in seasons.items():
        # Если n находится в массиве индексов месяцев сезона,
        # вернуть title имени сезона
        if n in month_indexes:
            return season_name.title()

    return "Нет такого месяца"


print(month_to_season(12))
