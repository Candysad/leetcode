#
# @lc app=leetcode.cn id=3081 lang=python3
#
# [3081] 替换字符串中的问号使分数最小
#
from heapq import *
# @lc code=start
class Solution:
    def minimizeStringValue(self, s: str) -> str:
        table = [0] * 26
        for c in s:
            if c != '?':
                c = ord(c) - ord('a')
                table[c] += 1
        queue = [(c, i) for i, c in enumerate(table)]
        heapify(queue)
        
        sub = []
        for c in s:
            if c == '?':
                count, c = heappop(queue)
                sub.append(chr(ord('a') + c))

                heappush(queue, (count + 1, c))
        sub.sort()
        
        j = 0
        result = ' '.join(s).split()
        for i, c in enumerate(result):
            if c == '?':
                result[i] = sub[j]
                j += 1
        
        return ''.join(result)       
# @lc code=end