import bisect


def findRadius(house:[int],heaters:[int]):
    min_range = 0
    house.sort()
    heaters.sort()
    for i in range(len(house)):
        insert_pos = bisect.bisect(heaters, house[i])
        if heaters[insert_pos-1] != house[i]:
            if len(heaters) > insert_pos:
                min_current = min(abs(house[i] - heaters[insert_pos-1]),abs(house[i] - heaters[insert_pos]))
            else:
                min_current = abs(house[i] - heaters[insert_pos-1])
            min_range = min_range if min_range > min_current else min_current
    return min_range


if __name__ =="__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(0,len(nums),2):
        house = [int(number) for number in nums[i].split(',')]
        heaters = [int(number) for number in nums[i+1].split(',')]
        print(findRadius(house,heaters))