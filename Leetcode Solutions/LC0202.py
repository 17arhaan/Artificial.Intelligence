# class Solution:
#     def isHappy(self , n:int ) -> bool:
#         current_n = n
#         number = 0
#         numbers = []
        
#         while True:
#             for digits in current_n:
#                 number += digits ** 2
#             if number == 1:
#                 return True
#             if number in numbers:
#                 return False
#             numbers[number] = 0
#             current_n = number
#             number = 0
        
# class Solution:
#     def isHappy(self , n:int ) -> bool:
#         current = n
#         number = 0
        
#         while True:
#             for i in range(str(current)):
#                 number = int(i) ** 2
#             if number == 1:
#                 return True
#             else:
#                 return False


class Solution(object):
    def isHappy(self, n):
        hset = set()
        while n != 1:
            if n in hset: return False
            hset.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        else:
            return True