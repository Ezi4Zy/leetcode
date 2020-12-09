#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = None
        for s in strs:
            if ret is None:
                ret = s
            else:
                i = 0
                while i < min(len(ret), len(s)):
                    if ret[i] != s[i]:
                        break
                    i += 1
                ret = ret[:i]
                if not ret:
                    return ret 
        return "" if ret is None else ret
                        
# @lc code=end

