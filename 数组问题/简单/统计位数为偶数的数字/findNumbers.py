class findNumbers:
    def findNumbers_1(num) -> int:
        """
        :param self:
        :param nums:
        :return:
        """
        count = 0
        lens = 0
        for i in num:
            str1 = str(i)
            if len(str1)%2 == 0:
                count +=1
        return count

    if __name__ == '__main__':
        with open('data.txt') as data:
            nums = data.read().split('\n')
        for i in range(len(nums)):
            numList = [int(number) for number in nums[i].split(',')]
            print(findNumbers_1(numList))