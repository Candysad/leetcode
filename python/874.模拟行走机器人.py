#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#
from collections import defaultdict
from sortedcontainers import SortedList
# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direct = 0
        obsx = defaultdict(SortedList)
        obsy = defaultdict(SortedList)
        
        for x, y in obstacles:
            if obsx[x].count(y): continue
            obsx[x].add(y)
            obsy[y].add(x)
        
        result = 0
        nowx, nowy = 0, 0
        for com in commands:
            if com == -1: # 0上，1右，2下，3左
                direct = (direct + 1) % 4
            elif com == -2:
                direct = (direct - 1) % 4
            else:
                if direct == 0:
                    obsi = obsx[nowx].bisect_left(nowy)
                    if obsi == len(obsx[nowx]):
                        nowy += com
                    else:
                        if obsx[nowx][obsi] == nowy:
                            obsi += 1
                        if obsi == len(obsx[nowx]):
                            nowy += com
                        else:
                            nowy = min(obsx[nowx][obsi] - 1, nowy + com)
            
                elif direct == 2:
                    obsi = obsx[nowx].bisect_left(nowy) - 1 
                    if obsi == -1:
                        nowy -= com
                    else:
                        if obsi == -1:
                            nowy -= com
                        else:
                            nowy = max(obsx[nowx][obsi] + 1, nowy - com)
                
                elif direct == 1:
                    obsi = obsy[nowy].bisect_left(nowx)
                    if obsi == len(obsy[nowy]):
                        nowx += com
                    else:
                        if obsy[nowy][obsi] == nowx:
                            obsi += 1
                        if obsi == len(obsy[nowy]):
                            nowx += com
                        else:
                            nowx = min(obsy[nowy][obsi] - 1, nowx + com)
            
                else:
                    obsi = obsy[nowy].bisect_left(nowx) - 1 
                    if obsi == -1:
                        nowx -= com
                    else:
                        if obsi == -1:
                            nowx -= com
                        else:
                            nowx = max(obsy[nowy][obsi] + 1, nowx - com)
                
                result = max(nowx**2 + nowy**2, result)
                print(nowx, nowy)
        return result

# @lc code=end