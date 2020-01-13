class Solution:
    def restoreIpAddresses(self, s: str) -> [str]:
        str_list = [int(i) for i in s]
        size = len(str_list)
        if size > 12 or size < 4:
            return []
        path = []
        res = []
        self.__dfs(str_list,0,size,path,res,1)
        res = [".".join([str(j) for j in i]) for i in res]
        return res

    def __dfs(self,str_list,start,size,path,res,pos):
        if len(path) == 4:
            res.append(path[:])
            return
        current_value = 0
        for i in range(start,size):
            for j in range(start,i+1):
                current_value = current_value*10 + str_list[j]
            if current_value == 0:
                if 4-pos <= size-1-start <= (4-pos) * 3:
                    path.append(current_value)
                    self.__dfs(str_list,i+1,size,path,res,pos+1)
                path.pop()
            elif current_value <= 255:
                if 4-pos <= size-1-start <= (4-pos) * 3:
                    path.append(current_value)
                    self.__dfs(str_list,i+1,size,path,res,pos+1)
                path.pop()
            else:
                path.pop()









if __name__ == "__main__":
    solution = Solution()
    res = solution.restoreIpAddresses("010010")
    print(res)
    