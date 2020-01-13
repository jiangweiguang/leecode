class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        size = len(nums)
        if size == 0:
            return []
        path = []
        res = []
        for i in range(size+1):
            self.__dfs(nums,0,size,path,res,0,i)
        return res

    def __dfs(self,nums,start,size,path,res,length,target):
        if length == target:
            res.append(path[:])
            return
        for i in range(start,size):
            path.append(nums[i])
            self.__dfs(nums,i+1,size,path,res,length+1,target)
            path.pop()

if __name__ == "__main__":
    solution = Solution()
    res = solution.subsets([1,2,3])
    print(res)
    