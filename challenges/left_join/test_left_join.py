from .hash_table import HashTable
from .left_join import left_join
import pytest


@pytest.fixture
def filled_table_one():
    table = HashTable()
    table.set('abc', 'bcd')
    table.set('qwert', 3)
    return table


@pytest.fixture
def filled_table_two():
    table = HashTable()
    table.set('abc', 'dsdf')
    table.set('qwert', '11')
    return table


@pytest.fixture
def filled_table_with_null():
    table = HashTable()
    table.set('qwert', '11')
    return table


def test_new(filled_table_one, filled_table_two):
    assert left_join(filled_table_one, filled_table_two) == [['abc', 'bcd', 'dsdf'], ['qwert', 3, '11']]


def test_new_with_none(filled_table_one, filled_table_with_null):
    assert left_join(filled_table_one, filled_table_with_null) == [['abc', 'bcd', None], ['qwert', 3, '11']]