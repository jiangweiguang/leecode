class Solution:
    def exist(self,board:[[str]],word:str):
        list_str = [i for i in word]
        size = len(board)
        if size == 0:
            return True
        path = []
        res = False
        path.append(list_str[0])
        test = [[0]*len(i) for i in board]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == list_str[0]:
                    test[i][j] = 1
                    if self.__dfs(board,list_str,i,j,path,1,test):
                        return True
                    test[i][j] = 0
        return False

    def __dfs(self,board,list_str,i,j,path,index,test):
        if list_str == path:
            return True
        if i-1 >= 0 and board[i-1][j] == list_str[index] and test[i-1][j] == 0:
            path.append(list_str[index])
            test[i-1][j] = 1
            if self.__dfs(board,list_str,i-1,j,path,index+1,test):
                return True
            test[i-1][j] = 0
            path.pop()
        if i + 1 < len(board) and board[i+1][j] == list_str[index] and test[i+1][j] == 0:
            path.append(list_str[index])
            test[i+1][j] = 1
            if self.__dfs(board, list_str, i + 1, j, path, index + 1,test):
                return True
            test[i+1][j] = 0
            path.pop()
        if j-1 >= 0 and board[i][j-1] == list_str[index] and test[i][j-1] == 0:
            path.append(list_str[index])
            test[i][j-1] = 1
            if self.__dfs(board, list_str, i, j-1, path, index + 1,test):
                return True
            test[i][j-1] = 0
            path.pop()
        if j+1 < len(board[i]) and board[i][j+1] == list_str[index] and test[i][j+1] == 0:
            path.append(list_str[index])
            test[i][j+1] = 1
            if self.__dfs(board, list_str, i, j+1, path, index + 1,test):
                return True
            test[i][j+1] = 0
            path.pop()
        return False



if __name__ == "__main__":
    solution = Solution()
    res = solution.exist([['a','b']],
                         "ba")
    print(res)
    