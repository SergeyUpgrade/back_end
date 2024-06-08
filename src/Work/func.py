import json
from datetime import datetime


def get_operations():
    """
    Загружаем json файл
    :return:
    """
    with open("operations.json", "r", encoding="UTF-8") as file:
        return json.load(file)


def get_last_5_executed(operations):
    """
    Сортируем загруженный файл сперва по значению 'EXECUTED',
    а потом по времени в порядке убывания и выводим пять первых значений
    :param operations:
    :return:
    """
    executed_operations = list(filter(lambda x: x.get('state') == 'EXECUTED', operations))
    executed_operations.sort(key=lambda x: datetime.fromisoformat(x['date']), reverse=True)
    last_5_executed = executed_operations[:5]
    return last_5_executed


def format_data(operation):
    """
    Преобразуем дату из формата "2018-03-23T10:45:06.972075" в "23.03.2018"
    :param operation:
    :return:
    """
    item = []
    for i in operation:
        get_date = i.get('date')
        split_date = get_date.split("T")[0].split("-")
        new_format = ".".join(split_date[::-1])
        i['date'] = new_format
        item.append(i)
    return item


def stealth_account_number(account_number: str):
    """
    Скрываем номер счета "Счет 41421565395219882431" -> "Счет **2431"
    :param account_number:
    :return:
    """
    info = account_number.split()
    return f"{info[0]} **{info[1][-4:]}"


def stealth_card_number(card_number: str):
    """
    Скрываем номер карты "Visa Classic 6831982476737658" -> "Visa Classic 6831 98** **** 7658"
    :param card_number:
    :return:
    """
    info = card_number.rsplit(" ", 1)
    return f"{info[0]} {info[1][0:4]} {info[1][4:6]}** **** {info[1][-4:]}"

# operation = get_operations()
# executed = get_last_5_executed(operation)
# new_data = format_data(executed)
#
# list(map(print, new_data))
