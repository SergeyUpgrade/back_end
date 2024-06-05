from Work.func import format_data

def test_format_data():
    assert format_data("2018-06-30T02:08:58.425572") == "30.06.2018"
