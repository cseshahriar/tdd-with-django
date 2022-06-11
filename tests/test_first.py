import pytest

def test_example():
    print("text_example")
    assert 1 == 1

# @pytest.mark.skip
@pytest.mark.slow
def test_example2():
    """ skip """
    assert 1 == 2