"""
思路：
首先观察测试用例[4,2,0,2,3,2,0]及预期结果[4,2,0,3,0,2,2]
从左到右第四个数字发生变化，且之后的数字按从小到大排列
所以必须先找出需要变化的位置以及填入的数字
找到需要变化的位置的方法：从由向左遍历列表，直到找到一个不满足从右向左看是递增的列表位置，该位置就是需要变换的位置
填入的数字：从右向左遍历列表的最后一个数字直到需要改变的那个位置的右边的位置，找到一个刚好比它大的数字，因为要遍历的列表显然满足递减规律，所以一找到该数，就把它与需要变化的位置的数字交换
将需要变换的位置之后的列表元素递增排序
"""
def nextPermutation(nums:[int]):
    len_nums = len(nums)
    if len_nums <= 1:
        return
    is_found = False
    swap_index = len_nums-1
    for i in range(len_nums-1,-1,-1):
        if i >0 and nums[i] >nums[i-1]:
            for j in range(len_nums-1,i-2,-1):
                if nums[j] > nums[i-1]:
                    nums[j],nums[i-1] = nums[i-1],nums[j]
                    is_found = True
                    swap_index = i -1
                    break
            if is_found:
                break
    if is_found:
        for i in range(swap_index+1, len_nums):
            min_value = nums[i]
            min_value_index = i
            for j in range(i + 1, len_nums):
                if nums[j] < min_value:
                    min_value = nums[j]
                    min_value_index = j
            nums[i], nums[min_value_index] = min_value, nums[i]
    else:
        nums.sort()
    return


if __name__ =="__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        data = [int(number) for number in nums[i].split(',')]
        nextPermutation(data)