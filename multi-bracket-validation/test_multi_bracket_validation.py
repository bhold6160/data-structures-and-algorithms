from multi_bracket_validation import multi_bracket_validation as mbv
import pytest

def test_multi_bracket_validation_true():
    """
    Tests a simple string for True validation
    """
    assert mbv('[()]') == True

def test_multi_bracket_validation_false():
    """
    Tests a simple string for False validation
    """
    assert mbv('[)') == False

def test_singlechar_bracket_validation():
    """
    Tests a single character string for False validation
    """
    assert mbv('}') == False

def test_multichar_bracket_validation_true():
    """
    Tests multi char string for True validation
    """
    assert mbv('[]([(qwerty)])()') == True

def test_multichar_bracket_validation_false():
    """
    Tests multi char string for False validation
    """
    assert mbv('[]([(qwerty)]})()') == False


