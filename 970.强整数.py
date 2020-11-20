#
# @lc app=leetcode.cn id=970 lang=python
#
# [970] 强整数
#

# @lc code=start

class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        # 0 <= bound <= 10^6
        # 2 ** 20 > bound
        ret = set()
        for i in range(20):
            for j in range(20):
                n = x ** i + y ** j
                if n <= bound:
                    ret.add(n)
                else:
                    break
                if y == 1:
                    break
            if x == 1:
                break
        return list(ret)

class Solution1(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        ret = set()
        x, y = max(x,y), min(x,y)
        i = 0
        j = 0
        while True:
            total = x ** i + y ** j
            if total <= bound:
                ret.add(total)
                if y != 1:
                    j += 1
                else:
                    if x != 1:
                        i += 1
                    else:
                        return list(ret)
            else:
                if j == 0:
                    return list(ret)
                else:
                    i += 1
                    j = 0
# @lc code=end

