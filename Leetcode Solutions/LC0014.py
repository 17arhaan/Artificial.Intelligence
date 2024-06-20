from typing import List

"""
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""

#todo Longest Common Prefix

#* Brute Force ----> Iterative Loops
#* Optimal Soln ---> Reference String

#! Brute Force Approach

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for string in strs[1:]:
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


#! Optimal Soln

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        
        first, last = strs[0], strs[-1]
        
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        return first[:i]