from .queue import Queue
import pytest

def test_make_invalid_queue():
    with pytest.raises(TypeError) as err:
        Queue(1)
    assert str(err.value) == 'Invalid iterable'

def test_start_queue():
    q = Queue([1, 2, 3])
    assert q.front.value == 1
    assert q.back.value == 3

def test_enqueue(small_queue):
    small_queue.enqueue(6)
    assert small_queue.front.value == 1
    assert small_queue.back.value == 6
    assert small_queue._size == 6

def test_enqueue_single(empty_queue):
    empty_queue.enqueue(38)
    assert empty_queue.front.value == 38
    assert empty_queue._size == 1

def test_enqueue_long(long_queue):
    long_queue.enqueue(10)
    assert long_queue.front.value == 1
    assert long_queue.back.value == 10
    assert long_queue._size == 10

def test_dequeue(small_queue):
    assert small_queue.dequeue() == 1
    assert small_queue._size == 4

def test_dequeue_values(small_queue):
    small_queue.dequeue()
    assert small_queue.front.value == 2
    assert small_queue.back.value == 5

def test_long_dequeue(long_queue):
    assert long_queue.dequeue()== 1
    assert long_queue._size == 8

def test_long_dequeue_values(long_queue):
    long_queue.dequeue()
    assert long_queue.front.value == 2
    assert long_queue.back.value == 9