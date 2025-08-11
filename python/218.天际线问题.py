#
# @lc app=leetcode.cn id=218 lang=python3
#
# [218] 天际线问题
#
from heapq import *
from collections import defaultdict
# @lc code=start
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        queue = []
        for left, right, h in buildings:
            points.append((left, h))
            points.append((right, -h))
            
            heappush(queue, (-h, left, right))
        
        result = defaultdict(int)
        points.sort()
        for p, h in points:
            t = queue.copy()
            if h > 0: # 左端点
                while t[0][1] > p or t[0][2] <= p: ### 有边界贴着左端点的情况也要跳过
                    heappop(t)
                result[p] = max(-t[0][0], result[p])
                
            else: # 右端点
                sign = 0
                while t:
                    if t[0][1] <= p and t[0][2] >= p: # 框住了
                        if -t[0][0] > -h: # 更高，没用了
                            sign = 1
                            break
                        elif t[0][2] > p: # 被更矮的拦截了，加入一个新的左端点
                            result[p] = -t[0][0]
                            sign = 1
                            break
                        else: 
                            heappop(t)
                    else: # 没框住
                        heappop(t)
                if sign == 0: # 没被拦住，加入一个 0
                    result[p] = max(0, result[p])
        
        result = sorted([[k, result[k]] for k in result])
        last = result[0]
        ans = []
        for now in result:
            sign = 0
            while ans:
                # 高度相同
                if ans and now[1] == ans[-1][1]:
                    if now[1] == 0:
                        ans.pop()
                    else:
                        sign = 1
                        break
                # 横坐标相同
                if ans and now[0] == ans[-1][0]:
                    ans.pop()
                else:
                    break
            if sign == 0:
                ans.append([now[0], now[1]])
        return ans
# @lc code=end

