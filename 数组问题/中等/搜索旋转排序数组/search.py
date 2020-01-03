def search(nums: [int], target: int):
    len_nums = len(nums)
    if nums is None:
        return -1

    left, right = 0, len_nums - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:  # 找到目标
            return mid
        elif nums[mid] > target:  # 比目标值大
            if nums[mid] >= nums[left]:  # 左边是有序的,注意区间长度为1的情况
                if nums[left] <= target:  # 目标值在有序序列范围内
                    right = mid - 1
                else:  # 目标值不在有序序列内，则查找右半部分
                    left = mid + 1
            else:  # 右边是有序的，而此时右边递增，所以不存在找到目标值的情况
                right = mid - 1
        else:  # 比目标值小
            if nums[mid] > nums[left]:  # 左边是有序的，此时左边递增，则目标值一定在右边
                left = mid + 1
            else:  # 右边是有序的
                if nums[right] >= target:  # 目标值在有序序列范围内
                    left = mid +1
                else:  # 目标值不在有序序列内，则查找右半部分
                    right = mid - 1
    return -1

if __name__ == "__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        data = [int(number) for number in nums[i].split(',')]
        target = data.pop()
        print(search(data, target))
