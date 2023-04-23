from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_product = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not set(words[i]) & set(words[j]):
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        return max_product


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
    print(solution.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
    print(solution.maxProduct(["a", "aa", "aaa", "aaaa"]))
