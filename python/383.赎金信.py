#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#
from collections import defaultdict
# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = defaultdict(int)
        for c in magazine:
            counter[c] += 1
        
        for c in ransomNote:
            if counter[c]:
                counter[c] -= 1
            else: return False
        
        return True
# @lc code=end