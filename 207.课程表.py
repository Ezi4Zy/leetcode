#
# @lc app=leetcode.cn id=207 lang=python
# 
# [207] 课程表
# 

# @lc code=start
import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for course1, course2 in prerequisites:
            graph[course2].append(course1)
        visited = [0] * numCourses
        
        def dfs(course):
            if visited[course] == 1:
                return False
            visited[course] = 1
            for c in graph[course]:
                if visited[c] == 0:
                    if not dfs(c):
                        return False
                elif visited[c] == 1:
                    return False
            visited[course] = 2
            return True

        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i):
                    return False
        return True

# @lc code=end

