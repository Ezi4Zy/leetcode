#
# @lc app=leetcode.cn id=1652 lang=python
#
# [1652] 拆炸弹
#

# @lc code=start
class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        leng = len(code)
        ret = [0] * leng
        
        for index in range(leng):
            if k > 0:
                if k + index >= leng:
                    ret[index] = sum(code[index+1:]) + sum(code[:k+index-leng+1])
                else:
                    ret[index] = sum(code[index+1:index+k+1])
            elif k < 0:
                tmp = -k
                if tmp > index:
                    ret[index] = sum(code[:index]) + sum(code[leng-tmp+index:])
                else:
                    ret[index] = sum(code[index-tmp:index])
        return ret

# @lc code=end

