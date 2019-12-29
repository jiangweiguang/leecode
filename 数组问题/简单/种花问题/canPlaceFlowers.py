def canPlaceFlowers(nums,key):
    count = 0
    for i,j in enumerate(nums):
        if j==1:
            continue
        else:
            if len(nums)>=2:
                if i == 0:
                    if nums[i+1] == 0:
                        count += 1
                        nums[i] =1
                        if count == key:
                            return True
                        continue
                    else:
                        continue
                elif i == len(nums)-1:
                    if nums[i-1] == 0:
                        nums[i] = 1
                        count += 1
                        if count == key:
                            return True
                        continue
                    else:
                        continue
                else:
                    if nums[i-1] ==nums[i+1] == 0:
                        nums[i] = 1
                        count +=1
                        if count == key:
                            return True
                        continue
                    else:
                        continue
            else:
                if key >1:
                    return False
                else:
                    return True
    return  False if key > count else True


if __name__ =="__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        data = [int(number) for number in nums[i].split(',')]
        key = data.pop()
        print(canPlaceFlowers(data,key))