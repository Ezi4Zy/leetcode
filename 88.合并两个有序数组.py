#
# @lc app=leetcode.cn id=88 lang=python
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        m_index = m - 1
        n_index = n - 1
        index = m + n - 1
        while index >= 0:
            if n_index >= 0:
                if m_index >= 0 and nums1[m_index] > nums2[n_index]:
                    nums1[index] = nums1[m_index]
                    m_index -= 1
                else:
                    nums1[index] = nums2[n_index]
                    n_index -= 1
            else:
                break
            index -= 1
 
# @lc code=end

