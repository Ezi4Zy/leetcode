#
# @lc app=leetcode.cn id=1461 lang=python
#
# [1461] 检查一个字符串是否包含所有长度为 K 的二进制子串
#

# @lc code=start
class Solution(object):
    
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(s) < (1 << k) + k - 1:
            return False
        cur = int(s[:k], base=2)
        codes = set([cur])
        begin = 0
        end = k
        while len(codes) != 2 ** k and end < len(s):
            cur = ((cur - (2 ** (k - 1)) * int(s[begin])) << 1) + int(s[end])
            codes.add(cur)
            end += 1
            begin += 1
        return len(codes) == 2 ** k
    
    def hasAllCodes1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        codes = set()
        index = 0
        while index <= len(s) - k and len(codes) != 2 ** k:
            codes.add(s[index:index+k])
            index += 1
        return len(codes) == 2 ** k


# @lc code=end

