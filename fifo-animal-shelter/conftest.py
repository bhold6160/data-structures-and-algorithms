import pytest
from fifo_animal_shelter import Animal as animal


@pytest.fixture
def empty_queue():
    """
    create an empty queue
    """
    return animal()


@pytest.fixture
def dcdc_queue():
    """
    create a short queue
    """
    return animal(['dog', 'cat', 'dog', 'cat'])


@pytest.fixture
def ddc_queue():
    """
    create a dog, dog, cat queue
    """
    return animal(['dog', 'dog', 'cat'])
