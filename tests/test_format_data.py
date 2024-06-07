from src.Work.func import format_data, stealth_account_number

def test_format_data():
    assert format_data("2018-06-30T02:08:58.425572") == "30.06.2018"

def test_stealth_account_number():
    assert stealth_account_number("Счет 78808375133947439319") == "Счет **9319"

