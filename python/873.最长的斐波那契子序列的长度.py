#
# @lc app=leetcode.cn id=873 lang=python3
#
# [873] 最长的斐波那契子序列的长度
#
from collections import defaultdict
# @lc code=start
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        atable = set(arr)
        table = defaultdict(lambda: defaultdict(int))
        
        n = len(arr)
        result = 0
        for i in range(n):
            right = arr[i]
            
            if table[right]:
                for left in table[right]:
                    ls = table[right][left] + 1
                    result = max(ls, result)
                    
                    if left+right in atable:
                        table[left + right][right] = max(table[left + right][right], ls)
            
            if 1 + n - i <= result: continue
            if i == n-1: break
            for j in range(i-1, -1, -1):
                left = arr[j]
                if left + right > arr[-1]: continue
                if left + right < arr[i+1]: break
                if left+right in atable:
                    table[left + right][right] = max(table[left + right][right], 2)
        return result
# @lc code=end