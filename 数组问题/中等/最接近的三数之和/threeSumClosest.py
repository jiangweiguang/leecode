def threeSumClosest(nums:[int],target:int):
    nums_len = len(nums)
    if nums_len < 3:
        return None
    nums.sort()
    most_close_target = nums[0] + nums[1] + nums[2]
    for index,value in enumerate(nums):
        left = index + 1
        right = nums_len -1
        while left < right:
            current_sum = nums[left] + value + nums[right]
            current_difference = current_sum - target
            most_close_difference = most_close_target-target
            abs_current = abs(current_difference)
            abs_most_close = abs(most_close_difference)
            if abs_current < abs_most_close:
                most_close_target = current_sum
            if current_difference == 0:
                return current_sum
            elif current_difference >0:
                right -= 1
            else:
                left += 1
    return most_close_target
if __name__ =="__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        data = [int(number) for number in nums[i].split(',')]
        target = data.pop()
        print(threeSumClosest(data,target))