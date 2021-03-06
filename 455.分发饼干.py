#
# @lc app=leetcode.cn id=455 lang=python
#
# [455] 分发饼干
#

# @lc code=start
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        ret = 0
        g.sort()
        s.sort()
        g_index = 0
        s_index = 0
        while g_index < len(g) and s_index < len(s):
            if g[g_index] <= s[s_index]:
                ret += 1
                g_index += 1
            s_index += 1
        return ret
# @lc code=end

