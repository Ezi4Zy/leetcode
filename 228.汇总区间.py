#
# @lc app=leetcode.cn id=228 lang=python
#
# [228] 汇总区间
#

# @lc code=start
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ret = []
        begin = None
        begin_index = None
        for index, num in enumerate(nums):
            if begin_index is not None:
                if num - begin != index - begin_index:
                    if index - 1 == begin_index:
                        ret.append(str(begin))
                    else:
                        ret.append(str(begin) + '->' + str(nums[index-1]))
                    begin = num
                    begin_index = index
            else:
                begin = num
                begin_index = index
        if begin_index is not None:
            if index == begin_index:
                ret.append(str(begin))
            else:
                ret.append(str(begin) + '->' + str(nums[index]))
        return ret
# @lc code=end

