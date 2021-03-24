#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        def dfs(nums, ans):
            if not nums:
                ret.append(ans)
            else:
                dfs(nums[1:], ans + nums[:1])
                dfs(nums[1:], ans)
        dfs(nums, [])
        return ret
# @lc code=end

