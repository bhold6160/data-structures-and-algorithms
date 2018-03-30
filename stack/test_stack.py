from .stack import Stack
from .node import Node
import pytest


def test_empty_stack_has_no_top(empty_stack):
    assert empty_stack.top is None


def test_push_to_empty(empty_stack):
    assert empty_stack.top is None
    assert empty_stack.push(1).value == 1

def test_push_invalid(small_stack):
    assert small_stack.push(None).value == 5


def test_empty_value_on_insert(empty_stack):
    with pytest.raises(TypeError):
        empty_stack.push()

def test_top_value(small_stack):
    assert small_stack.top.value == 5
    assert small_stack.top._next.value == 4

def test_pop(small_stack):
    assert small_stack.pop().value == 5
    assert small_stack.top.value == 4
    assert small_stack._size == 4


def test_single_pop(empty_stack):
    empty_stack.push(1)
    assert empty_stack.pop().value == 1
    assert empty_stack._size == 0

def test_peek(small_stack):
    assert small_stack.top.value is not None

