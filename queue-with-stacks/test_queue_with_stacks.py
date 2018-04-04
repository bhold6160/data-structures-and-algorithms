import pytest
from queue_with_stacks import Queue


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def small_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    return q


@pytest.fixture
def long_queue():
    q = Queue()
    for num in range(1, 10):
        q.enqueue(num)
    return q


def test_enqueue(small_queue):
    small_queue.enqueue(6)
    assert small_queue.front.value == 1
    assert small_queue.back.value == 6
    assert small_queue._size == 6