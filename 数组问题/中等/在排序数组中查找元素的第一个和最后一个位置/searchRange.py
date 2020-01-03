#该题直接不需要定义函数内函数也可以实现，空间复杂度应该会小一些
def searchRange(nums:[int],target:int)->[int]:
    if nums is None or len(nums) == 0:#如果列表为None或者长度为0，则直接返回[-1,-1]
        return [-1,-1]
    #找左边界
    def findleftRange(nums:[int],left,right,target):
        if nums[right] < target:#该列表最大值也没有target值大，则直接返回-1
            return -1
        while left <= right:#寻找target值
            mid = (left+right)//2
            if nums[mid] == target:#找到target值，对应索引为mid
                if mid-1>= left and nums[mid] == nums[mid-1]:#如果mid左边有数，且target值还在左边的列表中
                    right = mid -1
                else:#否则，mid值为左边界值
                    left =  mid
            elif nums[mid] > target:#如果target值大于mid值，则向左查找
                right = mid -1
            else:#如果target值小于mid值，则向右查找
                left = mid + 1
        return -1

    def findrightRange(nums:[int],left,right,target):
        if nums[left] > target:#最小值也比target值大，则找不到target值，返回-1
            return -1
        while left <= right:#寻找target值
            mid = (left+right)//2
            if nums[mid] == target:#找到target值，对应索引为mid
                if mid+1 <= right and nums[mid] == nums[mid+1]:#如果mid右边有数，且target值还在右边的列表中
                    left = mid +1
                else:#否则，mid值为右边界值
                    return mid
            elif nums[mid] > target:#如果target值大于mid值，则向左查找
                right = mid - 1
            else:#如果target值小于mid值，则向右查找
                left = mid + 1
        return -1
    left = findleftRange(nums,0,len(nums)-1,target)
    right = findrightRange(nums,0,len(nums)-1,target)
    return [left,right]


if __name__ == "__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        data = [int(number) for number in nums[i].split(',')]
        target = data.pop()
        print(searchRange(data,target))