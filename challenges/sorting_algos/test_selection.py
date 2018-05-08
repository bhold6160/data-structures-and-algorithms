from .selection import selection_sort


def test_empty_selection_sort():
    """
    Test empty selection sort
    """
    assert selection_sort([]) == []


def test_selection_sort_with_one_int():
    """
    Test selection sort with one int
    """
    assert selection_sort([67]) == [67]


def test_selection_sort_with_many_ints():
    """
    Test selection sort with many ints
    """
    assert selection_sort([3, 6, 1, 81, 17, 9]) == [1, 3, 6, 9, 17, 81]


def test_selection_sort_uneven_amount_of_ints():
    """
    Test selection sort with uneven amount of ints
    """
    assert selection_sort([18, 37, 11, 90, 78]) == [11, 18, 37, 78, 90]
