#
# @lc app=leetcode.cn id=2007 lang=python3
#
# [2007] 从双倍数组中还原原数组
#
from collections import Counter
from bisect import bisect_right
# @lc code=start
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2:
            return []
        counter = Counter(changed)
        changed.sort()
        
        i = 0
        result = []
        while i < n:
            num = changed[i]
            
            if counter[num]:
                if counter[2*num]:
                    counter[num] -= 1
                    result.append(num)
                    
                    counter[2*num] -= 1
                else:
                    return []
                
            i += 1
        
        return result
            
# @lc code=end

