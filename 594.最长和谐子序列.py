#
# @lc app=leetcode.cn id=594 lang=python
#
# [594] 最长和谐子序列
#

# @lc code=start
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        num_count = collections.Counter()
        for num in nums:
            num_count[num] += 1
        for num in num_count.keys():
            if num_count[num+1]:
                ret = max(ret, num_count[num+1] + num_count[num])
        return ret
# @lc code=end

