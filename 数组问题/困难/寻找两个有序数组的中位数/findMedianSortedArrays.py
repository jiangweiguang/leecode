def findMedianSortedArrays(nums1:[int],nums2:[int])->float:
#     def getKnum(array1:[int],array2:[int],index:int)->int:
#         len_1 = len(array1)
#         len_2 = len(array2)
#         lost_count = 0
#         start_1 = 0
#         start_2 = 0
#         while lost_count < index-1 and start_1 < len_1 and start_2 < len_2 :
#             k1 = (len_1-start_1) // 2
#             k2 = (len_2-start_2) // 2
#             temp_1 = array1[k1//2+start_1]
#             temp_2 = array2[k2//2+start_2]
#             if temp_1 < temp_2:
#                 start_1 = k1//2+start_1+1
#                 lost_count += start_1
#             elif temp_1 > temp_2:
#                 start_2 = k2//2+start_2+1
#                 lost_count += start_2
#             else:
#                 start_1 = k1 // 2 + start_1 + 1
#                 lost_count += start_1
#                 start_2 = k2 // 2 + start_2 + 1
#                 lost_count += start_2
#         if start_1 == len_1:
#             return array2[start_2+index-lost_count-1]
#         elif start_2 == len_2:
#             return array1[start_1 + index - lost_count-1]
#         else:
#             if lost_count == index -1:
#                 return array1[start_1] if array1[start_1] < array2[start_2] else array2[start_2]
#             else:
#                 return array1[start_1-1]
#     len1 = len(nums1)
#     len2 = len(nums2)
#     if len1 == 0:
#         if len2%2 == 0:
#             return (nums2[len2//2-1]+nums2[len2//2])/2
#         else:
#             return nums2[len2//2]
#     elif len2 == 0:
#         if len1%2 == 0:
#             return (nums1[len1//2-1]+nums1[len1//2])/2
#         else:
#             return nums1[len1//2]
#     else:
#         if (len1 + len2) % 2 == 0:
#             s = (len(nums1) + len(nums2)) // 2 + 1
#             value1 = getKnum(nums1,nums2,(len(nums1)+len(nums2))//2)
#             value2 = getKnum(nums1,nums2,s)
#             return (value1+value2)/2
#         else:
#             value1 = getKnum(nums1,nums2,(len(nums1)+len(nums2))//2 + 1)
#             return value1
#     def getKthNum(array1:[int],array2:[int],k:int)->float:
#         start_1 = start_2 = 0
#         end_1 = len(array1)
#         end_2 = len(array2)
#         lost_count = 0
#         while lost_count < k-1:
#             half_1 = (end_1-start_1)//2
#             half_2 = (end_2-start_2)//2
#             if start_1+half_1<end_1-1 and start_2+half_2 <end_2-1:
#                 if array1[start_1+half_1] == array2[start_2+half_2]:
#                     start_1 += half_1 + 1
#                     start_2 += half_2 + 1
#                     lost_count += half_1 + half_2
#                 elif array1[start_1+half_1] < array2[start_2+half_2]:
#                     start_1 += half_1+1
#                     lost_count += half_1
#                 else:
#                     start_2 += half_2 + 1
#                     lost_count += half_2
#             elif start_1+half_1 == end_1-1:
#                 start_2 += k - lost_count
#                 lost_count  == k-1
#             else:
#                 start_1 += k -lost_count
#                 lost_count == k-1
#         if lost_count == 0:
#             return  array1[0]
#         elif lost_count == k:
#             return  array1[start_1-1]
#         else:
#             result = array1[start_1] if array1[start_1] < array2[start_2] else array2[start_2]
#             return result
#     len_1 = len(nums1)
#     len_2 = len(nums2)
#     sum = len_1 + len_2
#     value1 = getKthNum(nums1,nums2,sum//2+1)
#     if sum%2 == 0:
#         value2 = getKthNum(nums1,nums2,sum//2)
#         return  (value1+value2)/2
#     else:
#         return value1
    def findKthElement(arr1,arr2,k):
        len1,len2 = len(arr1),len(arr2)
        if len1 > len2:
            return findKthElement(arr2,arr1,k)
        if not arr1:
            return arr2[k-1]
        if k == 1:
            return min(arr1[0],arr2[0])
        i,j = min(k//2,len1)-1,min(k//2,len2)-1#这里是我没有想到的地方
        if arr1[i] > arr2[j]:
            return findKthElement(arr1,arr2[j+1:],k-j-1)
        else:
            return findKthElement(arr1[i+1:],arr2,k-i-1)
    l1,l2 = len(nums1),len(nums2)
    left,right = (l1+l2+1)//2,(l1+l2+2)//2#这一步妙啊
    return (findKthElement(nums1,nums2,left)+findKthElement(nums1,nums2,right))/2


if __name__ =="__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(0,len(nums),2):
        data_0 = [int(number) for number in nums[i].split(',')]
        data_1 = [int(number) for number in nums[i+1].split(',')]
        print(findMedianSortedArrays(data_0,data_1))