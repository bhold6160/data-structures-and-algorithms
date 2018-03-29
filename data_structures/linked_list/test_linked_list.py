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

def test_insert(filled_linked_list):
    filled_linked_list.insert(16)
    assert filled_linked_list.head.data == 16

def test_find_list(filled_linked_list):
    assert filled_linked_list.find(3) == True
    
def test_empty_list(empty_linked_list):
    assert empty_linked_list.find(10) == False

def test_append(filled_linked_list):
    filled_linked_list.append(13)
    assert str(filled_linked_list) == str([1, 2, 3, 13])

def test_insert_before(filled_linked_list):
    filled_linked_list.insert_before(2, 36)
    assert str(filled_linked_list) == str([1, 36, 2, 3])

def insert_before_head(filled_linked_list):
    filled_linked_list.insert_before(1, 16)
    assert filled_linked_list.head == 16

def test_insert_after(filled_linked_list):
    filled_linked_list.insert_after(2, 10)
    assert filled_linked_list.head.next.next.data == 10

def test_insert_into_empty_ll(empty_linked_list):
    empty_linked_list.insert(4)
    assert empty_linked_list.head.data == 4

def test_merge_lists(filled_linked_list, more_filled_linked_list):
    merge_lists(filled_linked_list, more_filled_linked_list)
    assert str(filled_linked_list) == str([1, 5, 2, 6, 3, 7, 8, 9, 10 ,15])


def test_ll_kth_from_end(filled_linked_list):
    node_value = filled_linked_list.ll_kth_from_end(1)
    assert node_value.data == 2
