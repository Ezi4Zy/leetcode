#
# @lc app=leetcode.cn id=412 lang=python
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        for i in range(n+1)[1:]:
            if i % 3 != 0 and i % 5 != 0:
                ret.append(str(i))
            else:
                if i % 3 == 0 and i % 5 == 0:
                    ret.append('FizzBuzz')
                else:
                    if i % 3 == 0:
                        ret.append('Fizz')
                    else:
                        ret.append('Buzz')
        return ret
        
# @lc code=end

