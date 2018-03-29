import pytest
from .linked_list import LinkedList
from .ll_merge import merge_lists

@pytest.fixture
def filled_linked_list():
    return LinkedList([1, 2, 3])

@pytest.fixture
def empty_linked_list():
    return LinkedList()

@pytest.fixture
def more_filled_linked_list():
    return LinkedList([5, 6, 7, 8, 9 ,10, 15])

def test_find_list(filled_linked_list):
    assert filled_linked_list.find(1) == True
    
def test_empty_list(empty_linked_list):
    assert empty_linked_list.find(4) == False

def test_insert_into_empty_ll(empty_linked_list):
    empty_linked_list.insert(4)
    assert empty_linked_list.head.data == 4

def test_merge_lists(filled_linked_list, more_filled_linked_list):
    merge_lists(filled_linked_list, more_filled_linked_list)
    assert str(filled_linked_list) == str([1, 5, 2, 6, 3, 7, 8, 9, 10 ,15])


