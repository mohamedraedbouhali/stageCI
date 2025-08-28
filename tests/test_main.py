from CI import greet, add_numbers
def test_greet():
    """
    Test the greet function.
    """
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") != "Hello, Bob." # This test will pass

def test_add_numbers():
    """
    Test the add_numbers function.
    """
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(1.5, 2.5) == 4.0