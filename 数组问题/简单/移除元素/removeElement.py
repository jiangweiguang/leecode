def removeElement(nums,val):
    while val in nums:
        nums.remove(val)
    return len(nums)
if __name__ =="__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        data = [int(number) for number in nums[i].split(',')]
        val = data.pop()
        removeElement(data,val)