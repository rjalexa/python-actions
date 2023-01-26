from python_actions.add import add


def test_add():
    """test add function"""
    assert add(2, 3) == 5
    assert add("space", "ship") == "spaceship"
