from src.utils import for_from_card_and_account_coding


def test_for_from_card_and_account_coding():
    assert for_from_card_and_account_coding(dictionary=dict)[3]['from'] == 'Счет **9794'
    assert for_from_card_and_account_coding(dictionary=dict)[2]['from'] == 'Maestro 7810 84** **** 5568'
    assert for_from_card_and_account_coding(dictionary=dict)[1]['from'] == 'Visa Classic 2842 87** **** 9012'


def test_for_not_have_from():
    try:
        print(for_from_card_and_account_coding(dictionary=dict)[0]['from'])
    except KeyError:
        pass


