#
# @lc app=leetcode.cn id=520 lang=python
#
# [520] 检测大写字母
#

# @lc code=start
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        flag = None
        for index, c in enumerate(word):
            if index:
                if flag is None:
                    flag = c.isupper()
                else:
                    if c.isupper() != flag:
                        return False
            else:
                if c.islower():
                    flag = False
        return True
        
# @lc code=end

