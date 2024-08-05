from typing import List
"""
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
"""

#todo Relative Sort Array
    
#! Optimal Soln 

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        new_arr1 = []
        new_arr2 = []
        count = {num: 0 for num in arr1}
        for num in arr1:
            count[num] += 1
        
        for num in arr2:
            if num in count:
                new_arr1.extend([num] * count[num])
                del count[num]
        for num in sorted(count.keys()):
            new_arr2.extend([num] * count[num])
        
        return new_arr1 + new_arr2             
            