from src.utils import date_formatting


def test_date_formating():
    assert date_formatting(0)[3]['date'] == '2019.11.13'
    assert date_formatting(0)[4]['date'] == '2019.11.05'
    assert date_formatting(0)[0]['date'] == '2019.12.08'
