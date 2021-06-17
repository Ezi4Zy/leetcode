#
# @lc app=leetcode.cn id=1405 lang=python
#
# [1405] 最长快乐字符串
#

# @lc code=start
class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        d = {'a': a, 'b': b, 'c': c}
        ret = ""
        for _ in range(sum(d.values())):
            cand = set(['a', 'b', 'c'])
            if len(ret) > 1 and ret[-1] == ret[-2]:
                cand.remove(ret[-1])
            add_ = max(cand, key=lambda x: d[x])
            if d[add_] > 0:
                ret += add_
                d[add_] -= 1
            else:
                return ret
        return ret
        
# @lc code=end

