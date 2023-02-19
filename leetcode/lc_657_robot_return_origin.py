import pytest


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        origin = (0, 0)
        current_position = (0, 0)
        for direction in moves:
            match direction:
                case "U":
                    current_position = (current_position[0], current_position[1] + 1)
                case "D":
                    current_position = (current_position[0], current_position[1] - 1)
                case "L":
                    current_position = (current_position[0] - 1, current_position[1])
                case "R":
                    current_position = (current_position[0] + 1, current_position[1])

        return current_position == origin


# Testing
@pytest.mark.parametrize(
    "moves, expected",
    [
        ("UD", True),
        ("LL", False),
        ("RRDD", False),
        ("LDRRLRUULR", False),
    ],
)
def test_judgeCircle(moves, expected):
    assert Solution().judgeCircle(moves) == expected
