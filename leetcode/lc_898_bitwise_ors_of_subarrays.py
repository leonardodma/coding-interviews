from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        current = set()

        for num in arr:
            current = {num | x for x in current} | {num}
            result |= current

        return len(result)


if __name__ == "__main__":
    solution = Solution()
    print(solution.subarrayBitwiseORs([1, 1, 2]))
