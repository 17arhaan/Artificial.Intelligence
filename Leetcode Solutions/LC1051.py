'''
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match. 
'''
#todo  Height Check

#! Optimal Soln 

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        indices = 0
        for j in range(len(heights)):
            if heights[j] != expected[j]:
                indices += 1
        return indices
