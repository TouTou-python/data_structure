# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None
# #
# # class Solution:
# #     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
# #
# #         dummy = cur = ListNode(0)
# #         while l1 and l2:
# #             if l1.val < l2.val:
# #                 cur.next = l1
# #                 l1 = l1.next
# #             else:
# #                 cur.next = l2
# #                 l2 = l2.next
# #             cur = cur.next
# #         cur.next = l1 if l1 else l2
# #         return dummy.next
#
# class Stack:
#     def __init__(self):
#         self.stack = []
#         self.size = 0
#
#     def push(self,data):
#         self.stack.append(data)
#         self.size += 1
#
#     def pop(self):
#         if self.stack:
#             self.stack.pop()
#             self.size -= 1
#         else:
#             raise IndexError()
#
#     def peek(self):
#         return self.stack[-1]
#
#     def sizeof(self):
#         return self.size
#
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# class Link_Stack:
#     def __init__(self):
#         self.top = None
#         self.size = 0
#
#     def push(self,data):
#         new_node = Node(data)
#         if self.top:
#             new_node.next = self.top
#             self.top = new_node
#             self.size += 1
#         else:
#             self.top = new_node
#
#

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# a = a[1:]


class Solution:
    def threeSum(self, nums):

        n = len(nums)
        res = []
        if not nums or n < 3:
            return []
        nums.sort()
        res = []
        for i in range(n):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            light = i + 1
            right = n - 1
            while light < right:
                if nums[i] + nums[light] + nums[right] == 0:
                    res.append([nums[i], nums[light], nums[right]])
                    while light < right and nums[light] == nums[light + 1]:
                        light = light + 1
                    while light < right and nums[right] == nums[right - 1]:
                        right = right - 1
                    light = light + 1
                    right = right - 1
                elif nums[i] + nums[light] + nums[right] > 0:
                    right = right - 1
                else:
                    light = light + 1
        return res
