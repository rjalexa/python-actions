from python_actions.add import add


def test_add() -> None:
    """test add function"""
    assert add(2, 3) == 5
