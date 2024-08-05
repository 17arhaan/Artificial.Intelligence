# class Solution:
#     def numTeams(self, rating: List[int]) -> int:
#         n = len(rating)
#         count = 0
#         for i in range(n):
#             for j in range(i+1,n):
#                 for k in range(j+1,n):
#                     if (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]):
#                         count += 1
#         return count


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        
        for j in range(n):
            less_before = greater_before = 0
            less_after = greater_after = 0
            
            for i in range(j):
                if rating[i] < rating[j]:
                    less_before += 1
                elif rating[i] > rating[j]:
                    greater_before += 1
            
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    less_after += 1
                elif rating[k] > rating[j]:
                    greater_after += 1
            
            count += less_before * greater_after + greater_before * less_after
        
        return count
