from Fizz.fizz import fizz_buzz

def test_return_fizz():
    assert fizz_buzz(3) == "Fizz"

def test_return_buzz():
    assert fizz_buzz(5) == 'Buzz'

def test_return_fizzbuzz():
    assert fizz_buzz(15) == 'FizzBuzz'
