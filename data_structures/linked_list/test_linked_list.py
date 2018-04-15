import pytest
from .linked_list import LinkedList
from .ll_merge import merge_lists


@pytest.fixture
def filled_linked_list():
    """
    Fixture for short list
    """
    return LinkedList([1, 2, 3])


@pytest.fixture
def empty_linked_list():
    """
    fixture for empty list
    """
    return LinkedList()


@pytest.fixture
def medium_linked_list():
    """
    fixture for small list
    """
    return LinkedList([1, 2, 3, 4])


@pytest.fixture
def more_filled_linked_list():
    """
    Fixture for large list
    """
    return LinkedList([5, 6, 7, 8, 9, 10, 15])


def test_insert(filled_linked_list):
    """
    Inserts new value and returns its the new head
    """
    filled_linked_list.insert(16)
    assert filled_linked_list.head.data == 16


def test_find_list(filled_linked_list):
    """
    Checks if value passed in is in list
    """
    assert filled_linked_list.find(3) == True


def test_empty_list(empty_linked_list):
    """
    Checks if value is found in empty list
    """
    assert empty_linked_list.find(10) == False


def test_append(filled_linked_list):
    """
    Appends new value and returns new list
    """
    filled_linked_list.append(13)
    assert str(filled_linked_list) == str([1, 2, 3, 13])


def test_insert_before(filled_linked_list):
    """
    Inserts value before 2 and returns new list
    """
    filled_linked_list.insert_before(2, 36)
    assert str(filled_linked_list) == str([1, 36, 2, 3])


def insert_before_head(filled_linked_list):
    """
    Inserts 16 before one and returns new head
    """
    filled_linked_list.insert_before(1, 16)
    assert filled_linked_list.head == 16


def test_insert_after(filled_linked_list):
    """
    Inserts 10 after 2 and checks postion of new value
    """
    filled_linked_list.insert_after(2, 10)
    assert filled_linked_list.head.next.next.data == 10


def test_insert_into_empty_ll(empty_linked_list):
    """
    Inserts value into empty list and returns the head
    """
    empty_linked_list.insert(4)
    assert empty_linked_list.head.data == 4


def test_merge_lists(filled_linked_list, more_filled_linked_list):
    """
    Merges two lists together and returns new list
    """
    merge_lists(filled_linked_list, more_filled_linked_list)
    assert str(filled_linked_list) == str([1, 5, 2, 6, 3, 7, 8, 9, 10, 15])


def test_ll_kth_from_end(filled_linked_list):
    """
    Returns node the is 1 from the end
    """
    node_value = filled_linked_list.ll_kth_from_end(1)
    assert node_value == 2


def test_ll_did_not_find_loop(more_filled_linked_list):
    """
    Returns the list is not a loop
    """
    assert more_filled_linked_list.ll_find_loop() is False


def test_ll_find_loop(filled_linked_list):
    """
    Returns is the list is a loop
    """
    filled_linked_list.head.next.next.next = filled_linked_list.head
    assert filled_linked_list.ll_find_loop() is True


def test_kth_from_end_last(medium_linked_list):
    """
    test if inserted k from end of list
    """
    medium_linked_list.ll_kth_from_end(0)
    assert medium_linked_list.head.next.next.next.data == 4


def test_kth_from_end_second(medium_linked_list):
    """
    test if inserted k from end of list
    """
    medium_linked_list.ll_kth_from_end(2)
    assert medium_linked_list.head.next.data == 2


def test_kth_from_end_exception(medium_linked_list):
    """
    test if inserted k from end of list
    """
    with pytest.raises(AttributeError):
        medium_linked_list.ll_kth_from_end(6)
        medium_linked_list.ll_kth_from_end(-1)


def test_kth_from_end_invalid_type(medium_linked_list):
    """
    Test invalid input with a string
    """
    with pytest.raises(TypeError):
        medium_linked_list.ll_kth_from_end('a')
