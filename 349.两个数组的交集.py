#
# @lc app=leetcode.cn id=349 lang=python
#
# [349] 两个数组的交集
#

# @lc code=start

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        index1 = index2 = 0
        ret = []
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] == nums2[index2]:
                ret.append(nums1[index1])
                index1 += 1
                index2 += 1
            elif nums1[index1] < nums2[index2]:
                index1 += 1
            else:
                index2 += 1
            if ret:
                while index1 < len(nums1) and nums1[index1] == ret[-1]: 
                    index1 += 1
                while index2 < len(nums2) and nums2[index2] == ret[-1] :
                    index2 += 1
        return ret

class Solution1(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
        
# @lc code=end

