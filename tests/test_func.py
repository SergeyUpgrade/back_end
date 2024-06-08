from src.Work.func import get_operations, get_last_5_executed, format_data, stealth_account_number, stealth_card_number

def test_get_last_5_executed():
    assert get_last_5_executed([{"id": 441945886,"state": "EXECUTED","date": "2019-08-26T10:50:58.294041"},
                                {"id": 594226727,"state": "CANCELED","date": "2018-09-12T21:27:25.241689"},
                                {"id": 147815167,"state": "EXECUTED","date": "2018-01-26T15:40:13.413061"},
                                {"id": 649467725,"state": "EXECUTED","date": "2018-04-14T19:35:28.978265"},
                                {"id": 542678139,"state": "EXECUTED","date": "2018-10-14T22:27:25.205631"},
                                {"id": 41428829,"state": "EXECUTED","date": "2019-07-03T18:35:29.512364"}]) == [{"id": 441945886, "state": "EXECUTED","date": "2019-08-26T10:50:58.294041"},
                                                                                                                {"id": 41428829,"state": "EXECUTED","date": "2019-07-03T18:35:29.512364"},
                                                                                                                {"id": 542678139,"state": "EXECUTED","date": "2018-10-14T22:27:25.205631"},
                                                                                                                {"id": 649467725,"state": "EXECUTED","date": "2018-04-14T19:35:28.978265"},
                                                                                                                {"id": 147815167,"state": "EXECUTED","date": "2018-01-26T15:40:13.413061"},]

def test_format_data():
    assert format_data([{"date": "2019-08-26T10:50:58.294041"}, {"date": "2019-07-03T18:35:29.512364"}]) == [{"date": "26.08.2019"}, {"date": "03.07.2019"}]

def test_stealth_account_number():
    assert stealth_account_number("Счет 78808375133947439319") == "Счет **9319"

def test_stealth_card_number():
    assert stealth_card_number("MasterCard 1435442169918409") == "MasterCard 1435 44** **** 8409"
    assert stealth_card_number("Visa Gold 2684274847577419") == "Visa Gold 2684 27** **** 7419"

