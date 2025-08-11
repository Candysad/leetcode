#
# @lc app=leetcode.cn id=2055 lang=python3
#
# [2055] 蜡烛之间的盘子
#
from bisect import bisect_left
# @lc code=start
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        '''
        直接记录左右蜡烛位置和盘子的前缀和
        '''
        n = len(s)
        leftcandle = [-1] * n
        rightcandle = [-1] * n
        pres = [0] * n
        
        lasti = -1
        pre = 0
        for i, c in enumerate(s):
            if c == '|':
                lasti = i
            else:
                pre += 1
            
            leftcandle[i] = lasti
            pres[i] = pre
        for i in range(n, -1, -1):
            c = s[i]
            if c == '|':
                lasti = i
            rightcandle[i] = lasti
            
        result = [0] * len(queries)
        for i, (left, right) in enumerate(queries):
            l, r = -1, -1
            if leftcandle[left] != -1 and leftcandle[left] >= left:
                l = leftcandle[left]
            else:
                l = rightcandle[left]
            
            if rightcandle[right] != -1 and rightcandle[right] <= right:
                r = rightcandle[right]
            else:
                r = leftcandle[right]
            
            if l !=-1 and r!=-1 and l <= r:
                result[i] = max(0, pres[r] - pres[l])
            
        return result
        
        '''
        二分
        '''
        # n = len(s)
        # candles = []
        # cs = 0
        # for i, c in enumerate(s):
        #     if c == '|':
        #         candles.append(i)
        #         cs += 1
        # if cs == 0:
        #     return [0] * len(queries)

        # result = []
        # for left, right in queries:
        #     # 左
        #     li = bisect_left(candles, left)
        #     if li == cs:
        #         result.append(0)
        #         continue

        #     l = candles[li]
        #     if l >= right:
        #         result.append(0)
        #         continue
            
        #     # 右
        #     ri = bisect_left(candles, right)
        #     if ri != cs and candles[ri] == right:
        #         r = right
        #     else:
        #         ri -= 1
        #         r = candles[ri]

        #     if r > right:
        #         result.append(0)
        #         continue
            
        #     result.append(max(r-l-1 - (ri-li-1), 0))
        # return result    
# @lc code=end