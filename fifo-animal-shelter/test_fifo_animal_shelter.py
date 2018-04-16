from fifo_animal_shelter import Animal_Shelter as animal
import pytest


def test_empty_shelter(empty_queue):
    assert empty_queue.front is None
    assert empty_queue.back is None
    assert empty_queue._size == 0


def test_make_invalid_queue():
    """
    Test instantiating a new Animal Shelter with a non-iter will raise an error
    """
    with pytest.raises(TypeError) as err:
        animal(1)
    assert str(err.value) == 'Invalid iterable'


def test_instantiate_with_iterable():
    """
    Test instantiate wtih an iterable
    """
    animals = animal(['dog', 'dog', 'cat'])
    assert animals._size == 3
    assert animals.front.val == 'dog'
    assert animals.back.val == 'cat'


def test_enqueue(empty_queue):
    """
    Test enqueue into empty queue
    """
    empty_queue.enqueue('dog')
    assert empty_queue.front.val == 'dog'
    assert empty_queue._size == 1


def test_enqueue_invalid(dcdc_queue):
    """
    Test enqueue nothing
    """
    with pytest.raises(ValueError):
        dcdc_queue.enqueue(None)


def test_enqueue_invalid_animal(dcdc_queue):
    """
    Test enqueue not dog or cat
    """
    with pytest.raises(ValueError):
        dcdc_queue.enqueue('dat')


def test_enqueue_twice(empty_queue):
    """
    Test enqueue twice
    """
    empty_queue.enqueue('dog')
    empty_queue.enqueue('cat')
    assert empty_queue._size == 2
    assert empty_queue.front.val == 'dog'


def test_dequeue_none(dcdc_queue):
    """
    Test dequeue no pref
    """
    assert dcdc_queue.dequeue() == 'dog'
    assert dcdc_queue.front.val == 'cat'


def test_dequeue_invalid(empty_queue):
    """
    Test dequeue from empty
    """
    with pytest.raises(IndexError) as err:
        empty_queue.dequeue()
    assert str(err.value) == 'No animals'


def test_dequeue_dog(dcdc_queue):
    """
    Test dequeue front
    """
    assert dcdc_queue.dequeue('dog') == 'dog'
    assert dcdc_queue.front.val == 'cat'
    assert dcdc_queue._size == 3


def test_dequeue_cat(dcdc_queue):
    """
    Test dequeue not front
    """
    assert dcdc_queue.dequeue('cat') == 'cat'
    assert dcdc_queue._size == 3
    assert dcdc_queue.front.val == 'dog'


def test_dequeue_cat_vals(dcdc_queue):
    """
    Test dequeue not front
    """
    dcdc_queue.dequeue('cat')
    assert dcdc_queue.front._next.val == 'dog'
    assert dcdc_queue.front._next._next.val == 'cat'


def test_dequeue_cat_ddc(ddc_queue):
    """
    Test dequeue not front
    """
    assert ddc_queue.dequeue('cat') == 'cat'
    assert ddc_queue._size == 2


def test_dequeue_cat_ddc_vals(ddc_queue):
    """
    Test dequeue not front
    """
    ddc_queue.dequeue('cat')
    assert ddc_queue.front.val == 'dog'
    assert ddc_queue.front._next.val == 'dog'


def test_dequeue_dog_ddc(ddc_queue):
    """
    Test dequeue front
    """
    assert ddc_queue.dequeue('dog') == 'dog'
    assert ddc_queue.front.val == 'dog'
    assert ddc_queue._size == 2


def test_dequeue_invalid_animal(ddc_queue):
    """
    Test dequeue not string
    """
    with pytest.raises(TypeError):
        ddc_queue.dequeue(1)


def test_dequeue_not_dog_or_cat(ddc_queue):
    """
    Test dequeue not dog or cat
    """
    with pytest.raises(ValueError):
        ddc_queue.dequeue('dat')
