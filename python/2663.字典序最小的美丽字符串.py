#
# @lc app=leetcode.cn id=2663 lang=python3
#
# [2663] 字典序最小的美丽字符串
#

# @lc code=start
class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        k -= 1
        n = len(s)
        s = [ord(c) - ord('a') for c in s]
        
        sign1 = False
        for i in range(n-1, -1, -1):
            if s[i] < k:
                pre = set()
                if i - 1 >= 0: pre.add(s[i-1])
                if i - 2 >= 0: pre.add(s[i-2])
                
                t = s[i] + 1
                while t in pre:
                    t += 1
                if t <= k:
                    s[i] = t
                    sign1 = True
                    break
        
        if not sign1: return ''
        
        sign2 = False
        for j in range(i+1, n):
            pre = set()
            if j - 1 >= 0: pre.add(s[j-1])
            if j - 2 >= 0: pre.add(s[j-2])
            t = 0
            while t in pre:
                t += 1
                t %= 3
            s[j] = t
        
        return ''.join([chr(c+ord('a')) for c in s])    
# @lc code=end

