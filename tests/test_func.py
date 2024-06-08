from src.Work.func import get_operations, get_last_5_executed, format_data, stealth_account_number, stealth_card_number

def test_format_data():
    assert format_data("2018-06-30T02:08:58.425572") == "30.06.2018"

def test_stealth_account_number():
    assert stealth_account_number("Счет 78808375133947439319") == "Счет **9319"

def test_stealth_card_number():
    assert stealth_card_number("MasterCard 1435442169918409") == "MasterCard 1435 44** **** 8409"
    assert stealth_card_number("Visa Gold 2684274847577419") == "Visa Gold 2684 27** **** 7419"

