def findComplement(num:int):
    res = []
    bin_num = [int(i) for i in bin(num)[2:]]  # 获取二进制列表对应的数字
    for i in range(len(bin_num)):  # 按位取反
        res.append((bin_num[i]+1) % 2)  # 取反操作
    return int(''.join([str(j) for j in res]),2)  # 将结果转化为字符串，然后转为十进制


if __name__ =="__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        data = [int(number) for number in nums[i].split(',')]
        print(findComplement(data[0]))