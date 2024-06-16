
"""
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""

#todo Climbing Stairs

#* Brute Force ----> Recurssion
#* Optimal Soln ---> Dynamic Programming

#! Brute Force Approach

class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climb(n)
    
    def climb(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 1
        if n < 0:
            return 0
        
        # Recursive calls
        return self.climb(n - 1) + self.climb(n - 2)
    
#! Optimal Soln

class Solution:
    def climbStairs(self, n: int) -> int:
        one_step_before = 1
        two_steps_before = 1

        for i in range(2, n + 1):
            current = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = current
        
        return one_step_before