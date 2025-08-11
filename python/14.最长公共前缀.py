#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return strs[0]
        
        def check(s:str, pattern:str):
            if len(pattern) > len(s):
                return False
            if s[:len(pattern)] == pattern:
                return True
            return False
        
        result = ''
        for c in strs[0]:
            result += c
            for rest_str in strs[1:]:
                if check(rest_str, result) == False:
                    return result[:-1]
        return result
            
            
# @lc code=end

