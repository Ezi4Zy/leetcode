#
# @lc app=leetcode.cn id=709 lang=python
#
# [709] 转换成小写字母
#

# @lc code=start
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        ret = ""
        for c in str:
            if ord('A') <= ord(c) <= ord('Z'):
                ret += chr(ord(c) - (ord('A') - ord('a')))
            else:
                ret += c
        return ret
        
# @lc code=end

