def maxArea(height:[int]) -> int:
    """
    这里用到了动态规划，基本的表达式: area = min(height[i], height[j]) * (j - i)
    使用两个指针，值小的指针向内移动，这样就减小了搜索空间 因为面积取决于指针的距离与
    值小的值乘积，如果值大的值向内移动，距离一定减小，而求面积的另外一个乘数一定小于等
    于值小的值，因此面积一定减小，而我们要求最大的面积，因此值大的指针不动，而值小的指
    针向内移动遍
    """
    if len(height) <= 1:
        return False
    i,j,res = 0, len(height)-1, 0
    while i < j:
        h = min(height[i],height[j])
        res = max(res,h*(j-i))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return res

if __name__ =="__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        data = [int(number) for number in nums[i].split(',')]
        print(maxArea(data))