#
# @lc app=leetcode.cn id=1497 lang=python3
#
# [1497] 检查数组对是否可以被 k 整除
#
from collections import defaultdict
# @lc code=start
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        table = defaultdict(int)
        for num in arr:
            key = num % k
            otherkey = k - key
            if table[otherkey]:
                table[otherkey] -= 1
            else:
                table[key] += 1
        
        if table[0] % 2 == 0:
            table[0] = 0
        if any(table.values()):
            return False
        return True
        
# @lc code=end