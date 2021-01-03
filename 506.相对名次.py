#
# @lc app=leetcode.cn id=506 lang=python
#
# [506] 相对名次
#

# @lc code=start
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ret = []
        sorted_nums = sorted(nums, reverse=True)
        sorted_map = {}
        for index, num in enumerate(sorted_nums):
            sorted_map[num] = index
        for num in nums:
            sorted_index = sorted_map[num]
            if sorted_index == 0:
                ret.append("Gold Medal")
            elif sorted_index == 1:
                ret.append("Silver Medal")
            elif sorted_index == 2:
                ret.append("Bronze Medal")
            else:
                ret.append(str(sorted_index+1))
        return ret     
# @lc code=end

