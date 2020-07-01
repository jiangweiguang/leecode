class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        else:
            count = 0
            index = []
            for i in range(len(A)):
                if A[i] != B[i]:
                    count += 1
                    index.append(i) 
                if count > 2:
                    return False
            if count == 1:
                return False
            elif count == 0:
                dic = {}
                for i in A:
                    if i in dic:
                        dic[i] = dic[i] + 1
                    else:
                        dic[i] = 1
                for i in dic.values():
                    if i > 1:
                        return True
                return False
            else:
                if A[index[0]] == B[index[1]] and A[index[1]] == B[index[0]]:
                    return True
                else:
                    return False
                
if __name__ == "__main__":
    A = ""
    B = "ba"
    solution = Solution()
    re = solution.buddyStrings(A, B)
    print(re)