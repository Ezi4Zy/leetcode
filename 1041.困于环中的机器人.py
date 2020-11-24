#
# @lc app=leetcode.cn id=1041 lang=python
#
# [1041] 困于环中的机器人
#

# @lc code=start
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        directions = [0] * 4
        current_direction = 3
        for instruction in instructions:
            if instruction == 'G':
                directions[current_direction] += 1
            elif instruction == 'L':
                current_direction = (current_direction + 3) % 4
            else:
                current_direction = (current_direction + 1) % 4
        print current_direction, directions
        if current_direction != 3:
            return True
        if directions[0] == directions[2] and directions[1] == directions[3]:
            return True
        return False
# @lc code=end

