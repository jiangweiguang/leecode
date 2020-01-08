
def countPrimes(n:int):
    if n < 2:
        return 0
    nums = [1] * n
    nums[0] = nums[1] = 0
    for i in range(2,int(n**0.5)+1,1):
        if nums[i]:
            nums[i*i:n:i] = [0] * ((n-i*i-1)//i+1)
    return sum(nums)
if __name__ =="__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        data = [int(number) for number in nums[i].split(',')]