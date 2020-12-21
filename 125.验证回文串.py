#
# @lc app=leetcode.cn id=125 lang=python
#
# [125] 验证回文串
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        begin = 0
        end = len(s) - 1
        ord_a = ord('a')
        ord_z = ord('z')
        ord_A = ord('A')
        ord_Z = ord('Z')
        ord_0 = ord('0')
        ord_9 = ord('9')
        ignore_set = set([0, ord_a - ord_A, ord_A - ord_a])
        while end > begin:
            ord_begin = ord(s[begin])
            if not (ord_a <= ord_begin <= ord_z 
                    or ord_A <= ord_begin <= ord_Z
                    or ord_0 <= ord_begin <= ord_9):
                begin += 1
                continue
            ord_end = ord(s[end])
            if not (ord_a <= ord_end <= ord_z 
                    or ord_A <= ord_end <= ord_Z
                    or ord_0 <= ord_end <= ord_9):
                end -= 1
                continue
            if ord_0 <= ord_begin <= ord_9:
                if ord_begin != ord_end:
                    return False
            else:
                if ord_begin - ord_end not in ignore_set:
                    return False
            begin += 1
            end -= 1
        return True
# @lc code=end

