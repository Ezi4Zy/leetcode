#
# @lc app=leetcode.cn id=482 lang=python
#
# [482] 密钥格式化
#

# @lc code=start
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        dis = ord('A') - ord('a')
        ret = ""
        index = len(S) - 1
        count = 0
        while index >= 0:
            if S[index] != '-':
                if S[index].islower():
                    ret = chr(ord(S[index]) + dis) + ret
                else:
                    ret = S[index] + ret
                count += 1
                if count == K:
                    ret = '-' + ret
                    count = 0
            index -= 1
        return ret[1:] if ret and ret[0] == '-' else ret
# @lc code=end

