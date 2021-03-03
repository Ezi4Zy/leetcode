#
# @lc app=leetcode.cn id=12 lang=python
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = ""
        roman_map = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        for number in sorted(roman_map.keys(), reverse=True):
            roman_number = roman_map[number]
            if len(roman_number) == 1:
                if num >= number:
                    n = num / number
                    ret += n * roman_number
                    num -= n * number
            else:
                if num >= number:
                    ret += roman_number
                    num -= number
        return ret
       
# @lc code=end

