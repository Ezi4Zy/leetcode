#
# @lc app=leetcode.cn id=560 lang=python
#
# [560] 和为K的子数组
#

# @lc code=start
import collections
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre = 0
        ret = 0
        sums_map = collections.Counter()
        sums_map[0] = 1
        for index in range(len(nums)):
            pre += nums[index]
            ret += sums_map[pre-k]
            sums_map[pre] += 1
        return ret

# @lc code=end

