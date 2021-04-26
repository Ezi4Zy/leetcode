#
# @lc app=leetcode.cn id=416 lang=python
#
# [416] 分割等和子集
#

# @lc code=start
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 == 1:
            return False
        if len(nums) == 1:
            return False
        target = sum(nums) / 2
        max_num = max(nums)
        if max_num > target:
            return False
        if max_num == target:
            return True
        dp = [[False] * (target+1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(1, len(nums)):
            num = nums[i]
            for j in range(1, target+1):
                if j > num:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-num]
                elif j == num:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(nums)-1][target]
# @lc code=end

