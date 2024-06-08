from Work.func import get_operations, get_last_5_executed, format_data, stealth_account_number, stealth_card_number


def main():
    """
    Загружаем файл из json и выводим 5 последних выполненных операций с отформатированным временем,
    форматруем значения ключей "from" и "to" через функции stealth_account_number, stealth_card_number и принтуем результат
    :return:
    """
    get_operations_ = get_operations()
    get_last_5_executed_ = get_last_5_executed(get_operations_)
    formatted_last_5_operations = format_data(get_last_5_executed_)
    for i in formatted_last_5_operations:
        if "from" in i:
            get_from = i["from"]
            if "Счет" in get_from:
                i["from"] = stealth_account_number(i["from"])
            else:
                i["from"] = stealth_card_number(i["from"])
            if "Счет" in i["to"]:
                i["to"] = stealth_account_number(i["to"])
            else:
                i["to"] = stealth_card_number(i["to"])
            print(f"{i["date"]} {i["description"]}")
            print(f"{i["from"]} -> {i["to"]}")
            print(f"{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}\n")
        else:
            if "Счет" in i["to"]:
                i["to"] = stealth_account_number(i["to"])
            else:
                i["to"] = stealth_card_number(i["to"])
            print(f"{i["date"]} {i["description"]}")
            print(f"{i["to"]}")
            print(f"{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}\n")


if __name__ == "__main__":
    main()
