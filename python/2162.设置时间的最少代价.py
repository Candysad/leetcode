#
# @lc app=leetcode.cn id=2162 lang=python3
#
# [2162] 设置时间的最少代价
#

# @lc code=start
class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        # 按照分，秒一共四位数计算 cost
        def get(m1, m2, s1, s2):
            result = 0
            now = startAt
            # 分
            if m1 or m2:
                if m1 != 0 :
                    if m1 != now:
                        result += moveCost
                        now = m1
                    result += pushCost
                    
                    if now != m2:
                        result += moveCost
                        now = m2
                    result += pushCost
                
                else:
                    if now != m2:
                        result += moveCost
                        now = m2
                    result += pushCost
            
            # 秒
            # 前面按了
            if result:
                if now != s1:
                    result += moveCost
                    now = s1
                result += pushCost
                
                if now != s2:
                    result += moveCost
                    now = s2
                result += pushCost
            # 前面没按，只看后两个
            else:
                if s1 == 0:
                    if s2 != 0:
                        if now != s2:
                            result += moveCost
                            now = s2
                        result += pushCost
                else:
                    if now != s1:
                        result += moveCost
                        now = s1
                    result += pushCost
                
                    if now != s2:
                        result += moveCost
                        now = s2
                    result += pushCost
            return result
        
        # 太大，不能直接按，只能分1分钟给后面
        if targetSeconds >= 6000:
            secs = targetSeconds % 60 + 60
            mins = (targetSeconds - 60) // 60
            m2 = mins % 10
            m1 = mins // 10 % 10
            
            s2 = secs % 10
            s1 = secs // 10 % 10
            result = get(m1, m2, s1, s2)
            return result
        
        # 正常情况，直接按
        mins = targetSeconds // 60
        secs = targetSeconds % 60
        
        m2 = mins % 10
        m1 = mins // 10 % 10
        
        s2 = secs % 10
        s1 = secs // 10 % 10
        
        result = get(m1, m2, s1, s2)
        
        # 前面分一分钟给后面变成60秒
        if mins >= 1 and s1 <= 3:
            mins -= 1
            m2 = mins % 10
            m1 = mins // 10 % 10
            s1 += 6
            result = min(get(m1, m2, s1, s2), result)
        return result
# @lc code=end