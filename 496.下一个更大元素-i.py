#
# @lc app=leetcode.cn id=496 lang=python
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = []
        for num1 in nums1:
            for num2 in nums2[nums2.index(num1)+1:]:
                if num2 > num1:
                    ret.append(num2)
                    break
            else:
                ret.append(-1)
        return ret

# @lc code=end

