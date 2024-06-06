import json
from datetime import datetime

def get_operations():
    with open("operations.json", encoding="utf-8") as file:
        return json.load(file)


def get_last_5_executed(operations):
    executed_operations = list(filter(lambda x: x.get('state') == 'EXECUTED', operations))
    executed_operations.sort(key=lambda x: datetime.fromisoformat(x['date']), reverse=True)
    last_5_executed = executed_operations[:5]
    return last_5_executed


def format_data(srt_data: str):
    my_data = srt_data.split("T")[0].split("-")
    return ".".join(my_data[::-1])


def stealth_account_number(account_number):
    info = account_number.split()
    return f"{info[0]} **{info[1][-4:]}"

# "Visa Classic 6831982476737658"
def stealth_card_number(card_number):
    info = card_number.rsplit(" ", 1)
    return f"{info[0]} {info[1][0:4]} {info[1][4:6]}** **** {info[1][-4:]}"


print(stealth_card_number("Visa Classic 6831982476737658"))
