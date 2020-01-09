class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        list_str = list(s)
        list_p = list(p)
        len_str = len(list_str)
        len_p = len(list_p)
        path = []
        res = []
        self.__dfs()

    def __dfs(self,res_p,res_s,path,res):
        len_res_p = len(res_p)
        len_res_s = len(res_s)
        if len_res_p == len_res_s == 0:
            return True
        elif len_res_p > len_res_s:
            if len_res_s == 0:
                if res_p[0] == '*':
                    res_p.remove('*')
                    self.__dfs(res_p[1:],res_s,path,res)
                    res_p.insert(0,'*')
            else:
                 #if res_p[0] == '*':
                pass



if __name__ == "__main__":
    solution = Solution()
    res = solution
    