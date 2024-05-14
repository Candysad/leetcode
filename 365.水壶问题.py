#
# @lc app=leetcode.cn id=365 lang=python3
#
# [365] 水壶问题
#
from math import gcd
# @lc code=start
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        '''
        贝祖定理
        '''
        if z > x + y: return False
        if x == 0 or y == 0:
            return z == 0 or x+y == z
        return z % gcd(x, y) == 0
        
        
        '''
        带vis的深度优先
        '''
        stack = [(0,0)]
        vis = set()
        
        while stack:
            a, b = stack.pop()
            if a == target or b == target or a + b == target:
                return True
            
            vis.add((a,b))
            
            # 装满
            if (x, b) not in vis:
                stack.append((x,b))
            if (a, y) not in vis:
                stack.append((a, y))
            
            # a 倒进 b
            if a <= y-b: # 全倒
                if (0, a+b) not in vis:
                    stack.append((0, a+b))
            else: # 倒不完
                if (a - (y-b), y) not in vis:
                    stack.append((a-(y-b), y))
            
            # b 倒进 a
            if b <= y-a:
                if (a+b, 0) not in vis:
                    stack.append((a+b, 0))
            else:
                if (x, b-(x-a)) not in vis:
                    stack.append((x, b-(x-a)))
            
            # 清空
            if (0, b) not in vis:
                stack.append((0, b))
            if (a, 0) not in vis:
                stack.append((a, 0))
        
        return False
# @lc code=end

