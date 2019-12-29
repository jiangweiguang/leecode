def removeDuplicates(nums):
    """
    通过使用指针方式标记移动位置
    :param nums:
    :return:
    """
    value = -999999999999
    index = 0
    for i,j in enumerate(nums):
        if value == j:
            continue
        else:
            nums[index] = j
            value = j
            index += 1
    # for i in range(index):
    #     print(nums[i])
    return index
if __name__ =="__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        data = [int(number) for number in nums[i].split(',')]
        removeDuplicates(data)