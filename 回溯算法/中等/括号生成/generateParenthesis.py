class Solution:

    def generateParenthesis(self,n:int):
        if n == 0:
            return []
        path = []
        res = []
        self.__dfs(n,path,res,0,0)
        return res

    def __dfs(self,n,path,res,left,right):
        if left == right == n:  # 当左右括号匹配完成
            res.append("".join(path[:]))
        elif right < left < n:
            path.append('(')
            self.__dfs(n,path,res,left + 1,right)
            path.pop()
            path.append(')')
            self.__dfs(n,path,res,left,right+1)
            path.pop()
        elif right == left:
            path.append('(')
            self.__dfs(n, path, res, left + 1, right)
            path.pop()
        elif left == n:
            path.append(')')
            self.__dfs(n, path, res, left, right + 1)
            path.pop()


if __name__ =="__main__":
    solution = Solution()
    res = solution.generateParenthesis(3)
    print(res)