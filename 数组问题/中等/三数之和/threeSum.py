def threeSum(nums:[int]):
    n = len(nums)
    if n < 3:
        return []
    res = []
    nums.sort()
    for index,value in enumerate(nums):
        if value > 0:
            return res
        if index > 0 and nums[index-1] == value:
            continue
        left = index+1
        right = len(nums)-1
        while left < right:
            if nums[left] + value + nums[right] < 0:
                left += 1
            elif nums[left] + value + nums[right] == 0:
                res.append([value,nums[left],nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                left += 1
                while right > left and nums[right] == nums[right-1]:
                        right -= 1
                right -= 1
            else:
                right -= 1
    return res

if __name__ =="__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        data = [int(number) for number in nums[i].split(',')]
        print(threeSum(data))