import pysnooper
@pysnooper.snoop()
def fourSum(nums:[int],target:int):
    len_nums = len(nums)
    if len_nums < 4:
        return []
    res = []
    nums.sort()
    for i,j in enumerate(nums):
        if i > 0 and nums[i-1] == j:
            continue
        sub_target = target-j
        sub_nums = nums[i+1:]
        for index,value in enumerate(sub_nums):
            if index > 0 and sub_nums[index-1] == value:
                continue
            left = index +1
            right = len(sub_nums)-1
            while left < right:
                three_sum = sub_nums[index] + sub_nums[left] + sub_nums[right]
                if three_sum == sub_target:
                    res.append([nums[i],sub_nums[index],sub_nums[left],sub_nums[right]])
                    while left+1<right and sub_nums[left+1] == sub_nums[left]:
                        left += 1
                    while right-1 > left and sub_nums[right-1] == sub_nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif three_sum < sub_target:
                    left += 1
                else:
                    right -= 1
    return res

if __name__ =="__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        data = [int(number) for number in nums[i].split(',')]
        target = data.pop()
        print(fourSum(data,target))