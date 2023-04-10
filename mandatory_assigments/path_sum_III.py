from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.count = 0
        self.sum_counts = {0: 1}

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.pathSumRecursive(root, targetSum, 0)
        return self.count

    def pathSumRecursive(
        self, current_node: Optional[TreeNode], targetSum: int, current_sum: int
    ) -> None:
        if not current_node:
            return

        current_sum += current_node.val

        if current_sum - targetSum in self.sum_counts:
            self.count += self.sum_counts[current_sum - targetSum]

        if current_sum in self.sum_counts:
            self.sum_counts[current_sum] += 1
        else:
            self.sum_counts[current_sum] = 1

        self.pathSumRecursive(current_node.left, targetSum, current_sum)
        self.pathSumRecursive(current_node.right, targetSum, current_sum)

        self.sum_counts[current_sum] -= 1
