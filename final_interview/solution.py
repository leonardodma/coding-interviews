from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        for i in range(1, len(nums)):
            answer[i] = answer[i - 1] * nums[i - 1]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer


if __name__ == "__main__":
    s = Solution()
    answer = s.productExceptSelf([5, 2, 3, 4, 1])
    assert answer == [24, 60, 40, 30, 120]
