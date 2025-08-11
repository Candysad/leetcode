#
# @lc app=leetcode.cn id=3035 lang=python3
#
# [3035] 回文字符串的最大数量
#
from collections import Counter
# @lc code=start
class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        counter = Counter()
        
        table = []
        for word in words:
            counter.update(Counter(word))
            table.append(len(word))
        
        odd, even = 0, 0
        for v in counter.values():
            odd += v & 1
            even += v // 2
        
        result = 0
        table.sort()
        for limit in table:
            if odd:
                if limit // 2 <= even:
                    odd -= limit & 1
                    even -= limit // 2
                    result += 1
                else: return result
            else:
                if limit & 1:
                    even -= 1
                    odd += 2
                if limit // 2 <= even:
                    odd -= 1
                    even -= limit // 2
                    result += 1
                else: return result
            
        return result
# @lc code=end