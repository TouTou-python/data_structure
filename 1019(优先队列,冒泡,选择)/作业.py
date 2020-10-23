
# 颜色分类
# class Solution:
#     def sortColors(self, nums):
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] >= nums[j]:
#                     nums[i], nums[j] = nums[j], nums[i]
#         return nums


def sortColors(nums):
    a = c = 0
    b = len(nums) - 1
    while c <= b:
        if nums[c] == 0:
            nums[a], nums[c] = nums[c], nums[a]
            a += 1
            c += 1
        elif nums[c] == 2:
            nums[c], nums[b] = nums[b], nums[c]
            b -= 1
        else:
            c += 1


def f1(a, b):
    if a > b:
        a, b = b, a
    if b % a == 0:
        return a
    return f1(a, b % a)


def f2(a, b):
    if a > b:
        a,b = b,a
    if b - a == 0:
        return b
    return f2(b - a, a)


# 最长回文子串
# def longestPalindrome(strs):
#     length = len(strs)
#     if length < 2:
#         return strs
#     maxlen = 1
#     res = strs[0]
#     for i in range(length-1):
#         odd = centerSpread(strs, i, i)
#         even = centerSpread(strs, i, i + 1)
#         maxstr = odd if len(odd) > len(even) else even
#         if len(maxstr) > maxlen:
#             maxlen = len(maxstr)
#             res = maxstr
#     return res
#
#
# def centerSpread(strs, left, right):
#     length = len(strs)
#     i = left
#     j = right
#     while i >= 0 and j < length:
#         if strs[i] == strs[j]:
#             i -= 1
#             j += 1
#         else:
#             break
#     return strs[i+1:j]
#
# if __name__ == "__main__":
#     a = "2121212"
#     print(longestPalindrome(a))
