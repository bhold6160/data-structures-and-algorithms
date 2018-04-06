from towers_of_hanoi import towers_of_hanoi
import pytest


def test_towers_of_hanoi_two():
    """
    test checks disks end on target
    """
    assert towers_of_hanoi(2) == (3, [2, 1], [], [])


def test_towers_of_hanoi_three():
    """
    test checks disks end on target
    """
    assert towers_of_hanoi(3) == (7, [3, 2, 1], [], [])


def test_towers_of_hanoi_seven():
    """
    test checks disks end on target
    """
    assert towers_of_hanoi(7) == (127, [7, 6, 5, 4, 3, 2, 1], [], [])


def test_towers_of_hanoi_ten():
    """
    test checks disks end on target
    """
    assert towers_of_hanoi(10) == (
        1023, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [], [])
