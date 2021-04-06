#
# @lc app=leetcode.cn id=39 lang=python
#
# [39] 组合总和
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ret = []
        def dfs(candidates, target, ans, ret):
            if target == 0:
                ret.append(ans)
                return None
            for index, candidate in enumerate(candidates):
                if candidate <= target:
                    dfs(candidates[index:], target-candidate, ans + [candidate], ret)
            return None
        dfs(candidates, target, [], ret)
        return ret
# @lc code=end

