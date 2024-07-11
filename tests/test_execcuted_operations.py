import pytest

from src.utils import executed_operations


def test_executed_operations():
    assert executed_operations(dictionary=dict)[2]['state'] == 'EXECUTED'
    assert executed_operations(dictionary=dict)[6]['state'] == 'EXECUTED'
    assert executed_operations(dictionary=dict)[6]['id'] == 214024827


def test_executed_operations_more():
    with pytest.raises(IndexError):
        print(executed_operations(dictionary=dict)[86])



