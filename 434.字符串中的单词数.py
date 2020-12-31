#
# @lc app=leetcode.cn id=434 lang=python
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        flag = True
        for c in s:
            if flag and c != ' ':
                ret += 1
                flag = False
            elif not flag and c == ' ':
                flag = True
        return ret    
# @lc code=end

