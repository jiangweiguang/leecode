class Solution:
    def permute(self,nums:[int]):
        len_nums = len(nums)
        if len_nums == 0:
            return []
        path = []
        res = []
        self.__dfs(nums,path,res)
        return res

    def __dfs(self,nums,path,res):
        if len(nums) == 0:
            res.append(path[:])
        else:
            for i,j in enumerate(nums):
                path.append(j)
                nums.remove(j)
                self.__dfs(nums,path,res)
                nums.insert(i,j)
                path.pop()


if __name__ == "__main__":
    solution = Solution()
    res = solution.permute([1,2,3])
    print(res)

    