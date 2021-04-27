#
# @lc app=leetcode.cn id=494 lang=python
#
# [494] 目标和
#

# @lc code=start
class Solution(object):
    
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        pre_dp = [0] * 2001
        pre_dp[nums[0] + 1000] = 1
        pre_dp[-nums[0] + 1000] += 1
        for index in range(1, len(nums)):
            cur_dp = [0] * 2001
            for sum_ in range(-1000, 1001):
                if pre_dp[sum_ + 1000] > 0:
                    cur_dp[sum_ + nums[index] + 1000] += pre_dp[sum_ + 1000]
                    cur_dp[sum_ - nums[index] + 1000] += pre_dp[sum_ + 1000]
            pre_dp = cur_dp
        return pre_dp[S+1000] if S <= 1000 else 0
    
    def findTargetSumWays1(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if len(nums) == 1:
            if S == 0 and nums[0] == 0:
                return 2
            if nums[0] == S or nums[0] == -S:
                return 1
            else:
                return 0
        else:
            return self.findTargetSumWays(nums[:-1], S + nums[-1]) + self.findTargetSumWays(nums[:-1], S - nums[-1])

# @lc code=end

