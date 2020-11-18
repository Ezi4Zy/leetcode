#
# @lc app=leetcode.cn id=1437 lang=python
#
# [1437] 是否所有 1 都至少相隔 k 个元素
#

# @lc code=start
class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return True
        begin = 0
        while begin < len(nums):
            if nums[begin] == 1:
                if sum(nums[begin:begin+k+1]) != 1:
                    return False
                else:
                    begin += k
            else:
                begin += 1
        return True


class Solution1(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        pre = None
        for index, num in enumerate(nums):
            if num:
                if pre is not None and index - pre - 1 < k:
                    return False
                pre = index
        return True
# @lc code=end

