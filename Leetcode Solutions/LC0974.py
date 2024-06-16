
"""
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
"""

#todo Contiguos Sub Array

#* Brute Force ----> Iterative Loops
#* Optimal Soln ---> Hash Map

#! Brute Force Approach

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range (len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                if sum == k:
                    count +=1
        return count
    
#! Optimal Soln

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cumulative_sum = 0
        count = 0
        remainder_freq = [0] * k
        remainder_freq[0] = 1

        for num in nums:
            cumulative_sum += num
            remainder = cumulative_sum % k
            
            if remainder < 0:
                remainder += k
            
            count += remainder_freq[remainder]
            remainder_freq[remainder] += 1
        
        return count