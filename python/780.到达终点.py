#
# @lc app=leetcode.cn id=780 lang=python3
#
# [780] 到达终点
#

# @lc code=start
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:      
        while tx != ty and tx > sx and ty > sy:
            if tx > ty:
                tx %= ty 
            else:
                ty %= tx
                
        if sx == tx and sy == ty: return True
        
        if sx == tx:
            return ty > sy and (ty-sy) % tx == 0
        
        if sy == ty:
            return tx > sx and (tx-sx) % ty == 0
        
        return False
# @lc code=end