#
# @lc app=leetcode.cn id=961 lang=python
#
# [961] 重复 N 次的元素
#

# @lc code=start
class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()
        for num in nums:
            if num in num_set:
                return num
            num_set.add(num)
        return nums[0]

# @lc code=end

