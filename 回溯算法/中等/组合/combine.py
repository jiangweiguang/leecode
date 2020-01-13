class Solution:
    def combine(self,n:int,k:int):
        nums = [i for i in range(1,n+1)]
        path = []
        res = []
        start = 0
        self.__dfs(nums,k,start,n,path,res,0)
        return res

    def __dfs(self,nums,k,start,size,path,res,depth):
        if depth == k:
            res.append(path[:])  # 这里得创建一个新的列表
            return
        for i in range(start,size):
            path.append(nums[i])
            self.__dfs(nums,k,i+1,size,path,res,depth+1)
            path.pop()

if __name__ == "__main__":
    solution = Solution()
    res = solution.combine(4,2)
    print(res)
    