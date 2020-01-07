def uncommonFromSentences(A: str, B: str):
    A_list = A.split(' ')
    B_list = B.split(' ')
    for i in B_list:
        A_list.append(i)
    res = []
    dic = dict()
    for i in A_list:
        # if not dic.has_key(i): # python3以后删除了该方法
        #     dic[i] = 1
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for k in dic:
        if dic[k] == 1:
            res.append(k)
    return res


if __name__ == "__main__":
    A = "this apple is sweet"
    B = "this apple is sour"
    print(uncommonFromSentences(A, B))
