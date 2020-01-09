class Solution:
    def permuteUnique(self, nums: [int]) -> [[int]]:
        nums.sort()
        len_nums = len(nums)
        if len_nums == 0:
            return []
        path = []
        res = []
        self.__dfs(nums, path, res)
        return res

    def __dfs(self, nums, path, res):
        if len(nums) == 0:
            if path[:] not in res:
                res.append(path[:])
        else:
            for i, j in enumerate(nums):
                path.append(j)
                nums.remove(j)
                self.__dfs(nums, path, res)
                nums.insert(i, j)
                path.pop()

if __name__ == "__main__":
    solution = Solution()
    res = solution.permuteUnique([1,1,2])

