class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        nums = [int(i) for i in list(digits)]
        math = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'],
                ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'],
                ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        size = len(nums)
        if size == 0:
            return []
        path = []
        res = []
        self.__dfs(nums,0,size,path,res,math)
        return res
    def __dfs(self,nums,depth,size,path,res,math):  # """start,size"""
        # 当遍历完所有数字时
        if depth == size:
            res.append("".join(path[:]))
        else:
            for i in math[nums[depth]]:
                path.append(i)
                self.__dfs(nums,depth+1,size,path,res,math)
                path.pop()



if __name__ == "__main__":
    solution = Solution()
    res = solution.letterCombinations("23")
    print(res)
