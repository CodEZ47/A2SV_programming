"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_dict = dict()
        for emp in employees:
            emp_dict[emp.id] = emp
        
        val = 0
        
        def dfs(node):
            nonlocal val
            val += node.importance
            
            for sub in node.subordinates:
                dfs(emp_dict[sub])
        
        dfs(emp_dict[id])
        return val

    
                