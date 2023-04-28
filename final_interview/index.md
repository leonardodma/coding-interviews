# Product of Array Except Self

## Problem statement:

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

## Constraints:

- You must write an algorithm that runs in O(n) time

- You can not use the division operation to solve this problem

- 2 <= nums.length <= 105

- -30 <= nums[i] <= 30

## Reference:

[Leetcode 238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

## Hints:

- How can we calculate the product of all the elements to the left of a given index i?
- How can we calculate the product of all the elements to the right of a given index i?
- How can we combine the two ideas above to get the answer?

## Solution (without code):

- First, we initialize an array of length n, where n is the length of the input array, with all elements set to 1
- Then, we iterate over the input array, starting from the second element, and we update the answer array by multiplying the current element of the answer array by the previous element of the input array
- Then, we initialize a variable right to 1
- Then, we iterate over the input array, starting from the last element, and we update the answer array by multiplying the current element of the answer array by the variable right, and we update the variable right by multiplying it by the current element of the input array
- Finally, we return the answer array

## Time and space complexity:

- **Time complexity**: O(n), where n is the length of the input array
- **Space complexity**: O(n), where n is the length of the input array
