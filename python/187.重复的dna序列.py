#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#
from collections import defaultdict
# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []
        
        result = set()
        counter = defaultdict(int)
        for i in range(n-9):
            if counter[s[i:i+10]]:
                result.add(s[i:i+10])
            counter[s[i:i+10]] += 1
        
        return list(result)
# @lc code=end

