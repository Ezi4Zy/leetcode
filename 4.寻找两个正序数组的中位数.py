#
# @lc app=leetcode.cn id=4 lang=python
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        mid = (len(nums1) + len(nums2) + 1) / 2
        min_num = None
        flag = (len(nums1) + len(nums2)) % 2
        index1 = index2 = 0
        while index1 + index2 < mid:
            index1_num = nums1[index1] if index1 < len(nums1) else 10 ** 6
            index2_num = nums2[index2] if index2 < len(nums2) else 10 ** 6
            if index1_num > index2_num:
                min_num = index2_num
                index2 += 1
            else:
                min_num = index1_num
                index1 += 1

        if not flag:
            index1_num = nums1[index1] if index1 < len(nums1) else 10 ** 6
            index2_num = nums2[index2] if index2 < len(nums2) else 10 ** 6
            return float(min_num + min(index1_num, index2_num)) / 2
        else:
            return min_num   
# @lc code=end

