# class Array:
#     def __init__(self,capacity):
#         self.arrray = [None] * capacity
#         self.size = 0
#
#     def insert(self,index,data):
#         if index < 0 or index > self.size:
#             raise  IndexError("索引越界")
#         if self.size >= len(self.arrray) or index >= len(self.arrray):
#             self.addcapacity()
#         else:
#             for i in (self.size - 1 , index - 1 ,-1):
#                 self.arrray[i + 1] = self.arrray[i]
#             self.arrray[index] = data
#             self.size += 1
#
#     def remove(self,index):
#         if index < 0 or index > self.size:
#             raise  IndexError("索引越界")
#         for i in range(index,self.size):
#             self.arrray[i] = self.arrray[i + 1]
#         self.size -= 1
#
#     def out_put(self):
#         print(self.arrray)
#
#     def addcapacity(self):
#         new_array = [None] * self.arrray * 2
#         for i in range(self.size):
#             new_array[i] = self.arrray[i]
#         self.arrray = new_array


# 80
#     def removeDuplicates(self, nums: List[int]) -> int:
#         i = 0
#         for j in range(1, len(nums)):
#             # 无重复
#             if nums[i] != nums[j]:
#                 i += 1
#                 nums[i] = nums[j]
#             # 重复一次
#             elif i == 0 or nums[i-1] != nums[j]:
#                 i += 1
#                 nums[i] = nums[j]

#         return i + 1
# from  typing import List
#
#
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         slow = 0
#         fast = 1
#
#         while fast < len(nums):
#             if nums[slow] == nums[fast]:
#                 fast += 1
#                 while fast < len(nums) and nums[slow] == nums[fast]:
#                     for i in range(fast, len(nums) - 1):
#                         nums[i] = nums[i + 1]
#                 slow = fast
#                 fast += 1
#
#             else:
#                 slow += 1
#                 fast += 1
#         nums = nums[:-2]

a = [1,2,3,4,5]
a = a[:-1]
print(a)
