class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i+1 for i in range(n)]
        len_nums = len(nums)
        if len_nums == 0:
            return []
        path = []
        res = []
        stop = False
        self.__dfs(nums, path, res,k,stop)
        str_list = "".join([str(i) for i in res[-1]])
        return str_list


    def __dfs(self, nums, path, res,k,stop):
        if len(nums) == 0:
            res.append(path[:])
            if len(res) == k:
                stop = True
                return stop
        else:
            for i, j in enumerate(nums):
                path.append(j)
                nums.remove(j)
                stop = self.__dfs(nums, path, res,k,stop)
                if stop:
                    return stop
                nums.insert(i, j)
                path.pop()
if __name__ == "__main__":
    solution = Solution()
    res = solution.getPermutation(9,278082)
    print(res)
    