#
# @lc app=leetcode.cn id=300 lang=python
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution(object):
    
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        dp[0] = 1
        for index in range(1, len(nums)):
            dp[index] = 1
            for i in range(index):
                if nums[index] > nums[i]:
                    dp[index] = max(dp[index], dp[i]+1)
        return max(dp)
    
    def lengthOfLIS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[0,0] for _ in range(len(nums))]
        dp[0][0] = 0
        dp[0][1] = 1
        for index in range(1, len(nums)):
            dp[index][0] = max(dp[i][1] for i in range(index))
            dp[index][1] = 1 + max([0] + [dp[i][1] for i in range(index) if nums[i] < nums[index]])
        return max(dp[len(nums)-1])
            
# @lc code=end

