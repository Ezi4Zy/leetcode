#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#

# @lc code=start
class Solution(object):
    def generateParenthesis1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ["()"]
        else:
            ret = []
            for parentheses in self.generateParenthesis(n-1):
                for index in range(2 * (n - 1) + 1):
                    ret.append(parentheses[:index] + "()" + parentheses[index:])
            ret = list(set(ret))
            return ret
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        def generate(parentheses, left, right):
            if left < 0 or right < 0:
                return
            if not left and not right:
                ret.append(parentheses)
            else:
                if left == right:
                    generate(parentheses + '(', left - 1, right)
                else:
                    generate(parentheses + '(', left - 1, right)
                    generate(parentheses + ')', left, right - 1)
        generate('', n, n)
        return ret
        
# @lc code=end

