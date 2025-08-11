#
# @lc app=leetcode.cn id=2327 lang=python3
#
# [2327] 知道秘密的人数
#
from collections import deque
# @lc code=start
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10 ** 9 + 7
        queue = deque([1])
        window = 0
        last = 0
        for day in range(2, n+1):
            if day > forget:
                window -= queue.popleft()
                last -= 1
            if day > delay:
                window += queue[last] 
                last += 1
                
            queue.append(window % mod)
        
        return sum(queue) % mod
# @lc code=end