def buddyStrings(A:str,B:str):
    #长度不同时
    if len(A) != len(B):
        return False
    #两个字符串相等，若A中有重复元素，则返回TRUE
    if A == B and len(set(A)) < len(A):
        return True
    #使用zip进行匹配对比，挑出不同的字符对(python真的灵活啊）
    dif = [(a,b) for a,b in zip(A,B) if a != b]
    #对数只能为2，并且对称，如（a,b),(b,a)
    return len(dif) == 2 and dif[0] == dif[1][::-1]


if __name__ =="__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(0,len(nums),2):
        print(buddyStrings(nums[i],nums[i+1]))