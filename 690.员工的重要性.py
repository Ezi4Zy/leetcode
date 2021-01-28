#
# @lc app=leetcode.cn id=690 lang=python
#
# [690] 员工的重要性
#

# @lc code=start
"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        employee_importance_map = {}
        employee_subordinates_map = {}
        for employee in employees:
            employee_importance_map[employee.id] = employee.importance
            employee_subordinates_map[employee.id] = employee.subordinates
        employee_ids = [id]
        importance = 0
        while employee_ids:
            new_employee_ids = []
            for employee_id in employee_ids:
                importance += employee_importance_map[employee_id]
                new_employee_ids.extend(employee_subordinates_map[employee_id])
            employee_ids = new_employee_ids
        return importance
        
# @lc code=end

