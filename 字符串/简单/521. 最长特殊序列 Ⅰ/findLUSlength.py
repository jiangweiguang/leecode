class Solution:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def findLUSlength(self, s1, s2) -> int:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len != s2_len:
            return s1_len if s1_len > s2_len else s2_len
        else:
            if s1 == s2:
                return -1
            else:
                return s1_len


if __name__ == "__main__":
    s1 = "aaa"
    s2 = "aab"
    solution = Solution(s1, s2)
    s = solution.findLUSlength(s1, s2)
    print(s)
