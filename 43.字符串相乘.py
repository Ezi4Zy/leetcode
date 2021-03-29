#
# @lc app=leetcode.cn id=43 lang=python
#
# [43] 字符串相乘
#


# @lc code=start
class Solution(object):
    
    def add(self, num1, num2):
        flag = 0
        ret = ""
        length = min([len(num1), len(num2)])
        if length:
            for index in range(length):
                n1 = int(num1[-1 - index])
                n2 = int(num2[-1 - index])
                ret += str((n1 + n2 + flag) % 10)
                flag = (n1 + n2 + flag) / 10
            last_nums = num1[:-length] if len(num1) > length else num2[:-length]
        else:
            return num1 if len(num1) > length else num2
        return self.add(last_nums, str(flag) if flag else "") + ret[::-1]

    
    def multi(self, n, nums):
        ret = ""
        flag = 0
        for num in nums[::-1]:
            ret += str((int(num) * n + flag) % 10)
            flag = (int(num) * n + flag) / 10
        if flag:
            ret += str(flag)
        return ret[::-1]
        
    
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        multi_nums = [""] * 10
        multi_nums[0] = "0"
        ret = "0"
        num1, num2 = num1 if len(num1) < len(num2) else num2, num2 if len(num1) < len(num2) else num1
        for index, n in enumerate(num1[::-1]):
            n = int(n)
            if multi_nums[n]:
                num = multi_nums[n]
            else:
                num = self.multi(n, num2)
                multi_nums[n] = num
            num += "0" * index
            print ret, num
            ret = self.add(ret, num)
        return ret


# @lc code=end

