# #26 27 283
from typing import List
class Array:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("数组越界")
        if self.size >= len(self.array) or index >= len(self.array):
            self.addcapacity()
        for i in range(self.size - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = data
        self.size += 1

    def addcapacity(self):
        new_array = [None] * len(self.array) * 2
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array



    def remove(self, index):
        if index < 0 or index > self.size:
            raise Exception('数组越界')
        for i in range(index, self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def output(self):
        # for i in range(self.size):
            print(self.array)


array = Array(4)
array.insert(0, 0)
array.insert(0, 10)
array.insert(1, 1)
array.insert(2, 2)
array.insert(3, 3)

array.output()
#
#
class Solution:
    def removeDuplicates(self, nums: List[int]) :
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return nums,slow

aa = Solution()
a =[1, 1, 2, 3, 4]
aa.removeDuplicates(a)
print(aa.removeDuplicates(a))
#
# from typing import List
# class Solution:
#     def moveZeroes(self, nums1: List[int]):
#         i = 0
#         for j in range(len(nums1)):
#             if nums1[j] != 0:
#                 nums1[i], nums1[j] = nums1[j], nums1[i]
#                 i += 1
#         return nums1
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        fast = 1
        while fast < len(nums):
            if (nums[fast] - nums[slow]) == nums[fast] and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                fast += 1
                slow += 1
            elif nums[fast] != nums[slow]:
                fast += 1
                slow += 1
            else:

                fast += 1