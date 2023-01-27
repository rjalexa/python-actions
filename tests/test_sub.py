from python_actions.subtract import subtract


def test_sub() -> None:
    """test subtract function"""
    assert subtract(4, 3) == -1
