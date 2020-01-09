import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # nums = [i+1 for i in range(n)]
        # len_nums = len(nums)
        # if len_nums == 0:
        #     return []
        # path = []
        # res = []
        # stop = False
        # self.__dfs(nums, path, res,k,stop)
        # str_list = "".join([str(i) for i in res[-1]])
        # return str_list
        res = []
        pos = n
        path = [i for i in range(1,n+1)]
        while k > 0:
            pos -= 1
            cur = math.factorial(pos)
            if cur > k:
                res.append(path[0])
                path.remove(path[0])
            elif k % cur == 0:
                digit = k // cur
                res.append(path[digit-1])
                path.remove(path[digit-1])
                path.reverse()
                for i in path:  # 792346851
                    res.append(i)
                break
            else:
                digit = k //cur
                res.append(path[digit])
                path.remove(path[digit])
                pre = k//cur * cur
                k -= pre
        str_list = "".join([str(i) for i in res])
        return str_list






if __name__ == "__main__":
    solution = Solution()
    res = solution.getPermutation(9,278082)
    print(res)
    