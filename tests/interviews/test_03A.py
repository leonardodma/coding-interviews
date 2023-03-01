from interviews.interview_03A import StackWithMin
import pytest


def test_example():
    stack = StackWithMin()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    assert stack.minimum() == 1
    stack.pop()
    assert stack.minimum() == 2
    stack.pop()
    assert stack.minimum() == 3
    stack.pop()
    assert stack.minimum() == 4
    stack.pop()
    assert stack.minimum() == 5
    stack.pop()
    with pytest.raises(IndexError):
        stack.minimum()
