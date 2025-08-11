#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        快慢指针
        '''
        def change(num):
            result = []
            while num:
                result.append(num % 10)
                num//=10
            return sum([bit**2 for bit in result])
        
        n1, n2 = n, change(n)
        if n1 == 1 or n2 == 1: return True
        
        while n2 != 1:
            if n1 == n2: return False
            n1 = change(n1)
            n2 = change(change(n2))
        return True
        
        '''
        广度优先，但其实只有一种分支
        '''
        def change(num):
            result = []
            while num:
                result.append(num % 10)
                num//=10
            return sum([bit**2 for bit in result])

        vis = set()
        while n != 1:
            if n in vis: return False
            vis.add(n)
            n = change(n)
        return True  
# @lc code=end