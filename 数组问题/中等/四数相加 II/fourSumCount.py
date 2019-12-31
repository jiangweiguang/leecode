import collections
import pysnooper
# @pysnooper.snoop()
# def fourSumCount(A:[int],B:[int],C:[int],D:[int]):
#     len_list = len(A)
#     target = 0
#     count = 0
#     res = []
#     a_add_b = []
#     c_add_d = []
#     for i in range(len_list):
#         for j in range(len_list):
#             a_add_b.append(A[i]+B[j])
#             c_add_d.append(C[i]+D[j])
#     dic_one = dict()
#     for i,j in enumerate(a_add_b):
#         if j in dic_one:
#             dic_one[j].append(i)
#         else:
#             dic_one.setdefault(j,[]).append(i)
#     for i,j in enumerate(c_add_d):
#         if -j in dic_one:
#             count += len(dic_one[-j])
#     return count


def fourSumCount(A:[int],B:[int],C:[int],D:[int]):
    dic = collections.Counter(a + b for a in A for b in B)
    return sum(dic.get(-c-d,0) for c in C for d in D)


if __name__ =="__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(0,len(nums),4):
        A = [int(number) for number in nums[i].split(',')]
        B = [int(number) for number in nums[i+1].split(',')]
        C = [int(number) for number in nums[i+2].split(',')]
        D = [int(number) for number in nums[i+3].split(',')]
        print(fourSumCount(A,B,C,D))