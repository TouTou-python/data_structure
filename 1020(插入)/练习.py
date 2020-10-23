# from randList import randList
#
#
# def f(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums) - 1):
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#         print(nums)
#
#
# f(randList.randList(10))
#
#
# def f1(n):
#     for i in range(len(n)):
#         for j in range(i + 1, len(n) - 1):
#             if n[i] > n[j]:
#                 n[i], n[j] = n[j], n[i]
#         print(n)
#
#
# f(randList.randList(10))
#

# def twoSum(nums,target):
#     dic= {}
#     for i in range(len(nums)):
#         m = nums[i]
#         if target - m in dic:
#             return i , dic[m]
#         dic[m] = i


def minSubArrayLen( s, nums):
    b = 0
    for i in range(len(nums)):
        a = 0
        count = 0
        for j in range(i, len(nums)):
            a += nums[j]
            count += 1
            if a >= s:
                b = count
                if b >= count and a >= s:
                    b = count
    if b == 0:
        return 0

    return b



print(minSubArrayLen(15,[5,1,3,5,10,7,4,9,2,8]))