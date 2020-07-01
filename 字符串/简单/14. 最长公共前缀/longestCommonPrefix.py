class Solution:
    def __init__(self, strs):
        self.strs = strs
    def longestCommonPrefix(self, strs: [str]) -> str:
        lists = [list(str) for str in strs]
        lens = len(lists)
        if lens > 0:
            min_lens = len(lists[0])
        else:
            return ""
        for i in range(lens):
            if len(lists[i]) < min_lens:
                min_lens = len(lists[i])
        index = 0
        signal = 0
        while index < min_lens:
            charc = lists[0][index]
            for i in range(lens):
                if lists[i][index] != charc:
                    signal = 1
                    break
            if signal == 1:
                break
            else:
                index += 1
        return ''.join(lists[0][:index])

if __name__ == "__main__":
    strs = []
    solution = Solution(strs)
    re = solution.longestCommonPrefix(strs)
    print(re)