#
# @lc app=leetcode.cn id=2748 lang=python3
#
# [2748] 美丽下标对的数目
#
from collections import defaultdict
from math import gcd
# @lc code=start
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        table = defaultdict(int)
        result = 0
        
        for num in nums:
            first = int(str(num)[0])
            last = num % 10
            
            for i in range(10):
                if gcd(i, last) == 1:
                    result += table[i]
            
            table[first] += 1
                
        return result 
# @lc code=end