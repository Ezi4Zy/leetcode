#
# @lc app=leetcode.cn id=870 lang=python
#
# [870] 优势洗牌
#

# @lc code=start
import bisect
class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = [0] * len(nums1)
        nums1.sort()
        sorted_nums2 = sorted(nums2)
        for index2, num2 in enumerate(nums2):
            j = bisect.bisect_right(nums1, num2)
            if j < len(nums1):
                ret[index2] = nums1[j]
                nums1.pop(j)
            else:
                ret[index2] = nums1[0]
                nums1.pop(0)
        return ret


# @lc code=end

