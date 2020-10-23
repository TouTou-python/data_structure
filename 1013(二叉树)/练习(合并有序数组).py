from typing import List


class Solution:
    def merge(self, nums1, m, nums2, n):
        i, j = 0, 0
        while j < n:
            if i == m + j:
                nums1[i:m + n] = nums2[j:]
                return nums1
            if nums1[i] < nums2[j]:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                nums1.pop()
                i += 1
                j += 1

