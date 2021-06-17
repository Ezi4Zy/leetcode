#
# @lc app=leetcode.cn id=718 lang=python
#
# [718] 最长重复子数组
#

# @lc code=start
class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        len1, len2 = len(nums1), len(nums2)
        dp = [[0] * (len1 + 1) for _ in range(len2 + 1)]
        ret = 0
        for i in range(len2 - 1, -1, -1):
            for j in range(len1 - 1, -1, -1):
                dp[i][j] = (dp[i+1][j+1] + 1) if nums1[j] == nums2[i] else 0
                ret = max(ret, dp[i][j])
        return ret
# @lc code=end

