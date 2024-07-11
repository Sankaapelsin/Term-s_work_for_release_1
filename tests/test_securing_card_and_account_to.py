from src.utils import securing_card_and_account_to


def test_for_to_card_and_account_coding():
    assert securing_card_and_account_to(dictionary=dict)[3]['to'] == 'Счет **8125'
    assert securing_card_and_account_to(dictionary=dict)[2]['to'] == 'Счет **2869'
    assert securing_card_and_account_to(dictionary=dict)[1]['to'] == 'Счет **3655'
    assert securing_card_and_account_to(dictionary=dict)[4]['to'] == 'Счет **8381'
