#
# @lc app=leetcode.cn id=967 lang=python
#
# [967] 连续差相同的数字
#

# @lc code=start
class Solution(object):
    
    def bfs(self, next_, n, k):
        ans = []
        for i in next_:
            d = i % 10
            if d + k < 10:
                ans.append(i * 10 + d + k)
            if d - k >= 0 and k:
                ans.append(i * 10 + d - k)
        if n == 1:
            return ans
        else:
            return self.bfs(ans, n-1, k)    
    
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        if n == 0:
            return []
        if n == 1:
            return range(10)
        return self.bfs(range(1,10), n - 1, k)
        
# @lc code=end

