class Solution:
    def __init__(self, S):
        self.S = S
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        left = 0
        right = len(S) - 1
        while left < right:
            if not S[left].isalpha():
                left += 1
                continue
            b = ord(S[right])
            if not S[right].isalpha():
                right -= 1
                continue
            tmp = S[left]
            S[left] = S[right]
            S[right] = tmp
            left += 1
            right -= 1
        return ''.join(S)

if __name__ == "__main__":
    S = "7_28]"
    solution = Solution(S)
    re = solution.reverseOnlyLetters(S)
    print(re)