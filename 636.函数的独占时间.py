#
# @lc app=leetcode.cn id=636 lang=python
#
# [636] 函数的独占时间
#

# @lc code=start
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ret = [0] * n
        stack = []
        last_log = None
        for log in logs:
            log = log.split(':')
            func_id, is_start, timestamp = int(log[0]), log[1] == 'start', int(log[2])
            if is_start:
                if stack:
                    current_func_id = stack[-1][0]
                    if last_log[1]:
                        ret[current_func_id] += timestamp - last_log[2]
                    else:
                        ret[current_func_id] += timestamp - last_log[2] - 1
                stack.append((func_id, is_start, timestamp))
            else:
                current_func_id = func_id
                if last_log[1]:
                    ret[current_func_id] += timestamp - last_log[2] + 1
                else:
                    ret[current_func_id] += timestamp - last_log[2]
                stack.pop()
            last_log = (func_id, is_start, timestamp)
        return ret
# @lc code=end

