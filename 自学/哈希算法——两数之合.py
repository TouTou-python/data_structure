def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        m = nums[i]
        if target - m in dict:
            return dict[target - m], i
        dict[m] = i


# def twoSum1(nums, target):
#     start = 0
#     tail = len(nums) - 1
#     while start < tail:
#         temp = nums[start] + nums[tail]
#         if temp == target:
#             print(nums[start], nums[tail])
#             start += 1
#             tail -= 1
#         else:
#             if temp < target:
#                 start +=
#             else:
#                 tail -= 1
