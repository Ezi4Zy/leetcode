#
# @lc app=leetcode.cn id=824 lang=python
#
# [824] 山羊拉丁文
#

# @lc code=start
class Solution(object):

    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        VOWEL = 'aeiouAEIOU'
        ret = ''
        not_vowel = ''
        space = 0
        first_char = True
        for c in S:
            if first_char and c not in VOWEL:
                not_vowel = c
                first_char = False
            elif c == ' ':
                space += 1
                if not_vowel:
                    ret += not_vowel
                    not_vowel = ''
                ret +=  'ma' + 'a' * space + ' '
                first_char = True
            else:
                ret += c
                first_char = False
        else:
            space += 1
            if not_vowel:
                ret += not_vowel
                not_vowel = ''
            ret +=  'ma' + 'a' * space
        return ret
        
# @lc code=end

