#
# @lc app=leetcode.cn id=386 lang=python
#
# [386] 字典序排数
#

# @lc code=start
class Solution(object):

    def generate(self, start, n):
        ret = []
        start *= 10
        for i in range(10):
            if start + i == 0:
                continue
            if start + i <= n:
                ret.append(start + i)
                ret.extend(self.generate(start + i, n))
            else:
                break
        return ret

    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = self.generate(0, n)
        return ret

        
# @lc code=end

