import pytest


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        s_index = 0

        for char in t:
            if s[s_index] == char:
                s_index += 1
                if s_index == len(s):
                    return True

        return False


# Testing
@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
        ("", "ahbgdc", True),
        ("abc", "", False),
        ("abc", "ahbgdctttt", True),
    ],
)
def test_isSubsequence(s, t, expected):
    assert Solution().isSubsequence(s, t) == expected
