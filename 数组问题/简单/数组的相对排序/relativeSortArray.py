def relativeSortArray(list_1,list_2):
    dic = dict()
    new_list = []
    for i in list_2:
        dic[i] = 0
    for value in list_1:
        if value in dic:
            dic[value] +=1
        else:
            new_list.append(value)
    result_list = []
    for i in list_2:
        for j in range(dic[i]):
            result_list.append(i)
    new_list.sort()
    for i in new_list:
        result_list.append(i)
    return result_list
if __name__ =="__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    list_a = [int(number) for number in nums[0].split(',')]
    list_b = [int(number) for number in nums[1].split(',')]
    relativeSortArray(list_a,list_b)