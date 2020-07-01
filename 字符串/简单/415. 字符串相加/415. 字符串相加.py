class Solution:
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addStrings(self, num1: str, num2: str) -> str:
        num1 = [int(i) for i in list(num1)]
        num1.reverse()
        num2 = [int(i) for i in list(num2)]
        num2.reverse()
        num1_len = len(num1)
        num2_len = len(num2)
        signal = 0
        if num1_len > num2_len:
            for i in range(0, num2_len):
                num1[i] += num2[i] + signal
                signal = num1[i] // 10
                num1[i] %= 10
            for i in range(num2_len, num1_len):
                num1[i] += signal
                signal = num1[i] // 10
                num1[i] %= 10

            if signal != 0:
                num1.append(1)
            num1.reverse()
            num1 = [str(i) for i in num1]
            return "".join(num1)
        else:
            for i in range(0, num1_len):
                num2[i] += num1[i] + signal
                signal = num2[i] // 10
                num2[i] %= 10
            for i in range(num1_len, num2_len):
                num2[i] += signal
                signal = num2[i] // 10
                num2[i] %= 10

            if signal != 0:
                num2.append(1)
            num2.reverse()
            num2 = [str(i) for i in num2]
            return "".join(num2)


if __name__ == "__main__":
    num1 = "584"
    num2 = "18"
    solution = Solution(num1, num2)
    result = solution.addStrings(num1, num2)
    print(result)