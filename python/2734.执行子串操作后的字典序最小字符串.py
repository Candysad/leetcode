#
# @lc app=leetcode.cn id=2734 lang=python3
#
# [2734] 执行子串操作后的字典序最小字符串
#

# @lc code=start
class Solution:
    def smallestString(self, s: str) -> str:
        table = [chr((i-1) % 26+ ord('a')) for i in range(26)]
        
        n = len(s)
        for i in range(n):
            if s[i] > 'a':
                break
        
        if i == n-1:
            return s[:-1] + table[ord(s[-1]) - ord('a')]
        
        j = i + 1
        while j < n:
            if s[j] == 'a':
                break
            j += 1
        return s[:i] + ''.join([table[ord(c) - ord('a')] for c in s[i:j]]) + s[j:]
# @lc code=end