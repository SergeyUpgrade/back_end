from Work.func import get_operations, get_last_5_executed, format_data, stealth_account_number, stealth_card_number


def main():
    info = get_operations()
    info_1 = get_last_5_executed(info)
    info_2 = format_data(info_1)
    for i in info_2:
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

if __name__ == "__main__":
    main()
