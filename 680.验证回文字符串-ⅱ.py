#
# @lc app=leetcode.cn id=680 lang=python
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution(object):
    def validPalindrome(self, s, flag=True):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if flag:
                    return self.validPalindrome(s[left+1:right+1], flag=False) or self.validPalindrome(s[left:right], flag=False)
                else:
                    return False
        return True
# @lc code=end

