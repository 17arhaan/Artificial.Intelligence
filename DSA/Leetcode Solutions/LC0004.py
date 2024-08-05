from typing import List
"""
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""

#todo Median of Two Sorted Arrays

#* Brute Force ----> Hardcode Division
#* Optimal Soln ---> Binary Search

#! Brute Force Approach

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = nums1 + nums2
        combined.sort()
        n = len(combined)
        if n % 2 == 1:
            return combined[n // 2]
        else:
            mid1 = n // 2
            mid2 = mid1 - 1
            return (combined[mid1] + combined[mid2]) / 2.0

        
    
#! Optimal Soln 

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i
            
            maxLeftA = float('-inf') if i == 0 else nums1[i - 1]
            minRightA = float('inf') if i == m else nums1[i]
            maxLeftB = float('-inf') if j == 0 else nums2[j - 1]
            minRightB = float('inf') if j == n else nums2[j]
            
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2.0
                else:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                right = i - 1
            else:
                left = i + 1