class Solution:
    def __init__(self, s):
        self.s = s
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split()
        if len(s_list) == 0:
            return 0
        return len(s_list[-1])

if __name__ == "__main__":
    s = "Hello   "
    solution = Solution(s)
    word_len = solution.lengthOfLastWord(s)
    print(word_len)