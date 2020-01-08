class Solution:
    def combinationSum(self, candidates: [int], target: int):
        # res = []
        # candidates.sort()
        # if target > 0:
        #     if len(res) > 0 and i >= res[-1] and target - i >= 0:
        #         res.append(i)
        #         combinationSum(candidates,target -i)
        # elif target == 0:
        #     c
        #     return res
        # else:
        #     pass
        size = len(candidates)
        if size == 0:
            return []

            # 剪枝的前提是数组元素排序
            # 深度深的边不能比深度浅的边还小
            # 要排序的理由：1、前面用过的数后面不能再用；2、下一层边上的数不能小于上一层边上的数。
        candidates.sort()
        # 在遍历的过程中记录路径，一般而言它是一个栈
        path = []
        res = []
        # 注意要传入 size ，在 range 中， size 取不到
        self.__dfs(candidates, 0, size, path, res, target)
        return res


    # 递归回溯需要的：数组，开始点，长度，路径，结果集，目标值，使用另一个方法，就能够解决路径传递的问题
    def __dfs(self, candidates, begin, size, path, res, target):
        # 先写递归终止的情况
        if target == 0:
            # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
            # 或者使用 path.copy(),找到合适路径后，回溯到上一步，继续寻找合适路径
            res.append(path[:])

        for index in range(begin, size):  # 避免出现重复结果
            residue = target - candidates[index]
            # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行，这里并没有回溯，只是把该路径给剪枝了
            if residue < 0:
                break
            path.append(candidates[index])
            # 因为下一层不能比上一层还小，起始索引还从 index 开始，这里是我没想到应该这么做的
            self.__dfs(candidates, index, size, path, res, residue)
            path.pop()  # 这里体现回溯的想法，通过将该元素弹出，可以将下一个元素加入，从而达到遍历的效果


if __name__ == "__main__":
    solution = Solution()
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        data = [int(number) for number in nums[i].split(',')]
        target = data.pop()
        res = solution.combinationSum(data,target)
        print(res)
