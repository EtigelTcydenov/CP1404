"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # Test if Car sets the odometer correctly
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # Test if Car sets fuel correctly with a value passed in
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly with a value passed in"

    # Test if Car sets fuel correctly with the default value
    test_car = Car()
    assert test_car.fuel == 0, "Car does not set fuel correctly with the default value"

    # Test is_long_word function
    assert is_long_word("not") is False
    assert is_long_word("supercalifrag") is True
    assert is_long_word("Python", 6) is True

    # Test format_as_sentence function
    assert format_as_sentence('hello') == 'Hello.'
    assert format_as_sentence('It is an ex parrot.') == 'It is an ex parrot.'
    assert format_as_sentence('this is a valid test') == 'This is a valid test.'


# Uncomment the following line and run the doctests
doctest.testmod()

# Define the format_as_sentence function
def format_as_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a full stop.
    >>> format_as_sentence('hello')
    'Hello.'
    >>> format_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_as_sentence('this is a valid test')
    'This is a valid test.'
    """
    if not phrase:
        return ''

    formatted_phrase = phrase[0].upper() + phrase[1:]
    if formatted_phrase[-1] != '.':
        formatted_phrase += '.'

    return formatted_phrase

run_tests()
