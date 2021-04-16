#
# @lc app=leetcode.cn id=438 lang=python
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ret = []
        if len(s) < len(p):
            return ret
        p_counter = collections.Counter()
        for c in p:
            p_counter[c] += 1
        s_counter = collections.Counter()
        start = 0
        end = 0
        while end < len(p):
            s_counter[s[end]] += 1
            end += 1
        end -= 1
        while True:
            for k, v in p_counter.iteritems():
                if s_counter[k] != v:
                    break
            else:
                ret.append(start)
            end += 1
            if end >= len(s):
                break
            else:
                s_counter[s[end]] += 1
                s_counter[s[start]] -= 1
                start += 1
        return ret
            
# @lc code=end

