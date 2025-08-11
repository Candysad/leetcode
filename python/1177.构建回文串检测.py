#
# @lc app=leetcode.cn id=1177 lang=python3
#
# [1177] 构建回文串检测
#

# @lc code=start
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        pres = [0] * (n+1)
        
        pre = 0
        for i, c in enumerate(s):
            pre ^= 1 << (ord(c) - ord("a"))
            pres[i+1] = pre
        
        result = []
        for left, right, k in queries:
            t = pres[right+1] ^ pres[left]
            odd = t.bit_count() 
            if odd % 2: odd -= 1
            result.append(odd // 2 <= k)
        
        return result
# @lc code=end