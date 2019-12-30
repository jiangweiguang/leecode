def firstMissingPositive(nums:[int]) -> int:
    len_num = len(nums)
    for index, value in enumerate(nums):
        while nums[index] != index+1 and 1 <= nums[index] <= len_num:
            if nums[index] == nums[value-1]:
                break
            nums[index],nums[value-1] = nums[value-1],nums[index]
            value = nums[index]
    for i, j in enumerate(nums):
        if i+1 != j:
            return i+1
    return len_num+1

if __name__ =="__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        data = [int(number) for number in nums[i].split(',')]
        print(firstMissingPositive(data))