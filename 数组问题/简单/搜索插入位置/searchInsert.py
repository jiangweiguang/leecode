def searchInsert(nums: [int], target: int):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)
if __name__ == "__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        data = [int(number) for number in nums[i].split(',')]
