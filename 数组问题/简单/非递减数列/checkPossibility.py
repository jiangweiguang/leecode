def checkPossibility(nums):
    if len(nums)<=2:
        return True
    else:
        for index, value in enumerate(nums):
            if index+2 == len(nums):
                break
            else:
                if index+2 < len(nums):
                    a = nums[index]
                    b = nums[index+1]
                    c = nums[index+2]
                    if a<=b<=c:
                        continue
                    elif a<=c<=b or b<=a<=c:
                        nums[index+1] = nums[index]
                        break
                    elif b<=c<=a:
                        nums[index] = nums[index+1]
                        break
                    elif c<=a<=b:
                        nums[index+2] = nums[index+1]
                        break
                    elif c<b<a:
                        return False
                    elif b<a:
                        nums[index]= nums[index+1]
                        break
                    else:
                        nums[index+2] = nums[index+1]
                        break
                else:
                    break
        for index,value in enumerate(nums):
            if index+1 ==len(nums):
                break
            else:
                if value > nums[index+1]:
                    return False
        return True

if __name__ =="__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        data = [int(number) for number in nums[i].split(',')]
        print(checkPossibility(data))