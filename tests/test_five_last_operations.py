from src.utils import five_last_operations


def test_five_last_operations():
    assert five_last_operations(0)[0]['operationAmount']['currency']['name'] == 'USD'
    assert five_last_operations(0)[3]['description'] == 'Перевод со счета на счет'






