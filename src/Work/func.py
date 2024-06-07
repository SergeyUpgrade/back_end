import json
from datetime import datetime

def get_operations():
    with open("operations.json", "r", encoding="UTF-8") as file:
        return json.load(file)


def get_last_5_executed(operations):
    executed_operations = list(filter(lambda x: x.get('state') == 'EXECUTED', operations))
    executed_operations.sort(key=lambda x: datetime.fromisoformat(x['date']), reverse=True)
    last_5_executed = executed_operations[:5]
    return last_5_executed


def format_data(operation):
    item = []
    for i in operation:
        get_date = i.get('date')
        split_date = get_date.split("T")[0].split("-")
        new_format = ".".join(split_date[::-1])
        i['date'] = new_format
        item.append(i)
    return item


def stealth_account_number(account_number: str):
    info = account_number.split()
    return f"{info[0]} **{info[1][-4:]}"


def stealth_card_number(card_number: str):
    info = card_number.rsplit(" ", 1)
    return f"{info[0]} {info[1][0:4]} {info[1][4:6]}** **** {info[1][-4:]}"


# operation = get_operations()
# executed = get_last_5_executed(operation)
# new_data = format_data(executed)
#
# list(map(print, new_data))
