
#todo Two Sum

#* Brute Force ----> Double For - loop | O(n²)
#* Optimal Soln ---> Dictionary Storage | O(n)

#! Brute Force Approach

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums) - 1):
            for j in range(i+1 , len(nums)):
                if nums[i] + nums[j] == target:
                    return ([i , j])
        return False

#! Optimal Soln 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i , num in enumerate(nums):
            if target - num in visited:
                return ([visited[target - num] , i])
            elif num not in visited:
                visited[num] = i
    