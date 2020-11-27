#
# @lc app=leetcode.cn id=621 lang=python
#
# [621] 任务调度器
#

# @lc code=start
from heapq import *
from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        heap = []
        counter = Counter()
        for task in tasks:
            counter[task] += 1
        for task, count in counter.iteritems():
            heappush(heap, (-count, task))
        ret = 0
        while True:
            tasks = []
            for i in range(n+1):
                if heap:
                    count, task = heappop(heap)
                    count += 1
                    tasks.append((count, task))
            if tasks[0][0] == 0 and not heap:
                ret += len(tasks)
                break
            ret += n + 1
            for task_info in tasks:
                if task_info[0]:
                    heappush(heap, task_info)
        return ret
# @lc code=end

