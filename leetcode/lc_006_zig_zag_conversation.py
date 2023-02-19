class Solution:
    def convert(self, s: str, numRows: int) -> str:
        conversion_map = {}

        current_row = 0
        going_down = True

        for char in s:
            conversion_map.setdefault(current_row, []).append(char)
            current_row += 1 if going_down else -1

            if current_row == numRows - 1 or current_row == 0:
                going_down = not going_down

        return "".join([char for row in conversion_map.values() for char in row])
