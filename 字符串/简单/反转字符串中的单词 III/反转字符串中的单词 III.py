class Solution:
    def __init__(self,s):
        self.s = s

    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        s_list = [i[::-1] for i in s_list]
        s = ' '.join(s_list)
        return s


if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    solution = Solution(s)
    s = solution.reverseWords(s)
    print(s)