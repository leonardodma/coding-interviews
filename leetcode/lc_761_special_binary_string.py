class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count, i, res = 0, 0, []

        for j, number in enumerate(s):
            count += 1 if number == "1" else -1
            if count == 0:
                res.append("1" + self.makeLargestSpecial(s[i + 1 : j]) + "0")
                i = j + 1

        return "".join(sorted(res, reverse=True))


if __name__ == "__main__":
    solution = Solution()
    print(solution.makeLargestSpecial("11011000"))
