# from typing import List
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         # Base case: if the list is already sorted (0 or 1 elements), return it
#         if len(nums) <= 1:
#             return nums
        
#         # Split the list into two halves
#         mid = len(nums) // 2
#         left_half = self.sortArray(nums[:mid])
#         right_half = self.sortArray(nums[mid:])
        
#         # Merge the sorted halves
#         return self.merge(left_half, right_half)
    
#     def merge(self, left: List[int], right: List[int]) -> List[int]:
#         sorted_list = []
#         i = j = 0
        
#         # Merge the two lists while there are elements in both lists
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 sorted_list.append(left[i])
#                 i += 1
#             else:
#                 sorted_list.append(right[j])
#                 j += 1
        
#         # If there are remaining elements in the left list, add them
#         while i < len(left):
#             sorted_list.append(left[i])
#             i += 1
        
#         # If there are remaining elements in the right list, add them
#         while j < len(right):
#             sorted_list.append(right[j])
#             j += 1
        
#         return sorted_list


# from typing import List

# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         self.quickSort(nums, 0, len(nums) - 1)
#         return nums
    
#     def quickSort(self, nums: List[int], low: int, high: int):
#         if low < high:
#             pi = self.partition(nums, low, high)
#             self.quickSort(nums, low, pi - 1)
#             self.quickSort(nums, pi + 1, high)
    
#     def partition(self, nums: List[int], low: int, high: int) -> int:
#         pivot = nums[high]
#         i = low - 1
#         for j in range(low, high):
#             if nums[j] < pivot:
#                 i += 1
#                 nums[i], nums[j] = nums[j], nums[i]
#         nums[i + 1], nums[high] = nums[high], nums[i + 1]
#         return i + 1

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        else:
            pivot = nums[len(nums) // 2]
            left = [x for x in nums if x < pivot]
            middle = [x for x in nums if x == pivot]
            right = [x for x in nums if x > pivot]
            return self.sortArray(left) + middle + self.sortArray(right)
