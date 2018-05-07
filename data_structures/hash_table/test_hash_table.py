from hash_table import HT as HT
import pytest


def test_hash_size():
    """Hash autosizes."""
    ht = HT()
    assert ht.max_size == 1024


def test_hash_size2():
    """Size hash manaully."""
    ht = HT(2)
    assert ht.max_size == 2


def test_set_into_existing(test_hash):
    """Insert into existing hash."""
    assert test_hash.set('franky', 2) == {'franky': 2}


def test_size_of_default_hashtable():
    """Test size of default hashtable."""
    hashed = HT()
    assert len(hashed.buckets) == 1024


def test_size_of_hashtable_size_10():
    """Test size of hashtable with a size of 10."""
    hashed = HT(10)
    assert len(hashed.buckets) == 10


def test_size_of_hashtable_invalid_arguments():
    """Test construction of hashtable with invalid size argument."""
    with pytest.raises(TypeError):
        HT('dog')
