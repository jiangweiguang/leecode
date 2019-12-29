#使用list相关函数求解
def twoSum(numList,target):
    # nums.sort()
    lens = len(numList)
    j = -1
    for i in range(lens):
        aim = target - numList[i]
        if aim in numList:
            if(numList.count(aim) == 1)& (target == 2*numList[i]):
                continue
            else:
                j = numList.index(aim, i+1)
                break
    if j > 0:
        return [i,j]
    else:
        return []


#使用字典来做
def twoSum_2(self,numList,target)->[int]:
    """
    :param self:
    :param numList:
    :param target:
    :return: list[int]
    """
    hashmap = {}
    for index, num in enumerate(numList):
        another_num = target - num
        if another_num in hashmap:
            return [hashmap[another_num],index]
        hashmap[num] = index
    return None

if __name__ =="__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        numList = [int(number) for number in nums[i].split(',')]
        # print(type(numList[0]))
        target = numList.pop()
        # print(type(target))
        result = twoSum(numList,target)
        if result is None:
            print("not found")
        else:
            print(result)