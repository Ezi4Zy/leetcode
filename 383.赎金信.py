#
# @lc app=leetcode.cn id=383 lang=python
#
# [383] 赎金信
#

# @lc code=start
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        magazine_counter = collections.Counter()
        for c in magazine:
            magazine_counter[c] += 1
        for c in ransomNote:
            magazine_counter[c] -= 1
        return all([count >= 0 for count in magazine_counter.values()])    
# @lc code=end

