#
# @lc app=leetcode.cn id=242 lang=python
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_dic = collections.Counter()
        for c in s:
            s_dic[c] += 1
        for c in t:
            s_dic[c] -= 1
            if s_dic[c] < 0:
                return False
        return sum(s_dic.values())  == 0
# @lc code=end

