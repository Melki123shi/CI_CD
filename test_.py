import pytest
import fizzBuzz
@pytest.mark.parametrize("input,expected", [
    (1, "1"),
    (2, "2"),
    (3, "Fizz"),
    (4, "4"),
    (5, "Buzz"),
    (6, "Fizz"),
    (10, "Buzz"),
    (15, "FizzBuzz"),
    (30, "FizzBuzz"),
])
def test_fizzbuzz(input, expected):
    assert fizzBuzz.fizz_buzz(input) == expected