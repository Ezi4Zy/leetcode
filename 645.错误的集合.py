#
# @lc app=leetcode.cn id=645 lang=python
#
# [645] 错误的集合
#

# @lc code=start
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        miss_num = None
        repeat_num = None
        max_num = len(nums)
        no_repeat_nums = list(set(nums))
        complete_nums_sum = max_num * (max_num+1) / 2
        miss_num =  complete_nums_sum - sum(no_repeat_nums)
        repeat_num = sum(nums) - sum(no_repeat_nums)
        return [repeat_num, miss_num]
        
# @lc code=end

