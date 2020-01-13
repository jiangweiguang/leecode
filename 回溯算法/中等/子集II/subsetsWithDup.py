class Solution:
    def subsetsWithDup(self, nums: [int]) -> [[int]]:
        nums.sort()
        size = len(nums)
        if size == 0:
            return []
        path = []
        res = []
        for i in range(size + 1):
            self.__dfs(nums, 0, size, path, res, 0, i)
        return res

    def __dfs(self, nums, start, size, path, res, length, target):
        if length == target:
            res.append(path[:])
            return
        for i in range(start, size):
            # 这里是去重的重点
            if start <i and nums[i-1] == nums[i]:
                continue
            path.append(nums[i])
            self.__dfs(nums, i + 1, size, path, res, length + 1, target)
            path.pop()

if __name__ == "__main__":
    solution = Solution()
    res = solution.subsetsWithDup([1,2,2])
    print(res)