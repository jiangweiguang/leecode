class Solution:
    def __init__(self, A, B):
        self.A = A
        self.B = B


    def repeatedStringMatch(self, A: str, B: str) -> int:
        A_size = len(A)
        B_size = len(B)
        final_index = 0
        while len(A) < 2 * A_size + B_size:
            A += A[:A_size]
        A_index = B_index = B_size - 1  # 连续等的方式是可以赋值的，不公用内存地址
        A_len = len(A)
        A = list(A)
        B = list(B)
        while A_index < A_len:
            while B_index >= 0 and A[A_index] == B[B_index]:
                A_index -= 1
                B_index -= 1
            if B_index < 0:
                final_index = A_index + B_size
                if (final_index + 1) % A_size == 0:
                    return (final_index + 1) // A_size
                else:
                    return (final_index + 1) // A_size + 1
            elif B_index == B_size - 1:
                while B_index >= 0:
                    if A[A_index] == B[B_index]:
                        break
                    else:
                        B_index -= 1
                shift1 = (B_size - 1 - B_index)
                A_index += shift1
                B_index = B_size -1
            else:
                #  获取坏字符位移
                shift1 = shift2 = 0
                while B_index >= 0:
                    if A[A_index] == B[B_index]:
                        break
                    else:
                        B_index -= 1
                shift1 = (B_size - 1 - B_index)
                #  获取好后缀位移
                B_index = B_size - 2
                while B_index >= 0:
                    if A[A_index] == B[B_index]:
                        break
                    else:
                        B_index -= 1
                shift2 = B_size - 1 - B_index
                shift = shift1 if shift1 > shift2 else shift2
                A_index += shift
                B_index = B_size -1
        return -1







if __name__ == "__main__":
    A = "aabaa"
    B = "aaab"
    solution = Solution(A, B)
    re = solution.repeatedStringMatch(A, B)
    print(re)