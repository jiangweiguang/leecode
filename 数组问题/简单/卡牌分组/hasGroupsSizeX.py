def hasGroupsSizeX(nums):
    def gcd(m,n):
        while n != 0:
            rem = m % n
            m = n
            n = rem
        return m
    dic = dict()
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    # if len(dic) == 1 :
    #     if dic[nums[0]] == 1:
    #         return False
    #     else:
    #         return True
    # else:
    #     temp = gcd()
    list = []
    for key,value in dic.items():
       list.append(value)
    if len(list) == 1:
        if list[0] == 1:
            return False
        else:
            return True
    else:
        mid = list[0]
        for i in list:
            mid = gcd(mid,i)
        if mid > 1:
            return True
        else:
            return False
#欧几里得求最大公约数

if __name__ =="__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        data = [int(number) for number in nums[i].split(',')]
        print(hasGroupsSizeX(data))