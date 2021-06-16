#
# @lc app=leetcode.cn id=997 lang=python
#
# [997] 找到小镇的法官
#

# @lc code=start
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        judges = set(range(1,n+1))
        not_judges = set([i[0] for i in trust])
        judges -= not_judges
        if judges:
            judge_map = {}
            for j in judges:
                judge_map[j] = set()
            for t in trust:
                if t[1] in judges:
                    judge_map[t[1]].add(t[0])
            ret = -1
            for j in judge_map:
                if len(judge_map[j]) == n - 1:
                    if ret != -1:
                        return -1
                    else:
                        ret = j
            return ret
        else:
            return -1
# @lc code=end

