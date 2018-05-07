from hash_table import HashTable as HT
import pytest


@pytest.fixture
def test_hash():
    """
    Test hash table.
    """
    ht = HT()
    ht.set('ted', 9)
    ht.set('jones', 3)
    ht.set('extravaganza', 4)
    return ht
