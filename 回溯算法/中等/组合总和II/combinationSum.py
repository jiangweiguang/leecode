class Solution:

    def combinationSum2(self, candidates: [int], target: int):
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        path = []
        res = []
        self.__dfs(candidates, 0, size, path, res, target)
        return res

    # 这里self不能少，是用来调用自身的
    def __dfs(self, candidates, start, size, path, res, target):
        if target == 0:
            res.append(path[:])
            # return

        for i in range(start, size):
            if target - candidates[i] < 0:         # 这里不是很懂啊
                break
            if i > start and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            # 注意这里的start为i+1,即从当前位置的下一个位置开始找起
            self.__dfs(candidates, i + 1, size, path, res, target - candidates[i])
            path.pop()


if __name__ == "__main__":
    solution = Solution()
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        data = [int(number) for number in nums[i].split(',')]
        target = data.pop()
        res = solution.combinationSum2(data, target)
        print(res)
