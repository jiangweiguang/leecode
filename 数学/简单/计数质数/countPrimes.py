def countPrimes(n:int):
    if n <=2:
        return 0
    # dic = dict(zip([i for i in range(2,n,1)],[1 for i in range(2,n,1)]))
    dic = dict(zip([i for i in range(2,n,1)],[1]*(n-2)))
    i = 0
    count = n-2
    for key in dic.keys():
        if key > int(n**2)+1:
            break
        if dic[key] == 0:
            continue
        aim = key * 2
        while aim < n:
            if dic[aim] == 1:
                dic[aim] = 0
                count -= 1
            aim += key
    return count




if __name__ =="__main__":
    # with open('data.txt') as data:
    #     nums = data.read().split('\n')
    # for i in range(len(nums)):
    #     data = [int(number) for number in nums[i].split(',')]
    print(countPrimes(10))