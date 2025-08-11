#
# @lc app=leetcode.cn id=1871 lang=python3
#
# [1871] 跳跃游戏 VII
#
from collections import deque
# @lc code=start
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1': return False
        n = len(s)
        
        
        window = deque([c=='0' for c in s[:minJump]])
        windowlimit = maxJump - minJump + 1
        windowvalue = 1
        count = 1
        
        now = minJump
        while now < n:
            if s[now] == '0' and now:
                window.append(True)
            else:
                window.append(False)
            now += 1
            
            if window[count]:
                windowvalue += 1
                count += 1
            
            if count == windowlimit + 1:
                t = window.popleft()
                if t:
                    windowvalue -= 1
                count -= 1
        
        return window[-1] 
# @lc code=end