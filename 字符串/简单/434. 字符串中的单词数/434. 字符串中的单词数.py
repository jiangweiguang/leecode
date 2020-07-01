class Solution:
    def __init__(self,s):
        self.s = s
    def countSegments(self, s: str) -> int:
        list = s.split()
        return len(list)


if __name__ == "__main__":
    s = "Hello, my name is John"
    solution = Solution(s)
    re = solution.countSegments(s)
    print(re)