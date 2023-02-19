import pytest
from leetcode.lc_006_zig_zag_conversation import Solution


@pytest.mark.parametrize(
    "s, num_rows, expected",
    [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("PAYPALISHIRING", 5, "PHASIYIRPLIGAN"),
        ("A", 1, "A"),
    ],
)
def test_zig_zag_conversion(s, num_rows, expected):
    assert Solution().convert(s, num_rows) == expected
