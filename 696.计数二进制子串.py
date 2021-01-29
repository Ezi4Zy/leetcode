#
# @lc app=leetcode.cn id=696 lang=python
#
# [696] 计数二进制子串
#

# @lc code=start

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        index = 0
        pre_count = 0
        next_count = 0
        c = s[index]
        while index < len(s) and s[index] == c:
            index += 1
            pre_count += 1
        while index < len(s):
            while index < len(s) and s[index] != c:
                index += 1
                next_count += 1
            ret += min(pre_count, next_count)
            pre_count, next_count, c = next_count, 0, s[index-1]
        return ret

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        index = 0
        next_diff_index = 0
        current_c = s[index]
        while next_diff_index < len(s) and s[next_diff_index] == current_c:
            next_diff_index += 1
        while index < len(s):
            current_c = s[index]
            diff_ = next_diff_index - index
            index = next_diff_index
            while next_diff_index < len(s) and s[next_diff_index] != current_c:
                next_diff_index += 1
            ret += min(diff_, next_diff_index - index)
        return ret

# @lc code=end

