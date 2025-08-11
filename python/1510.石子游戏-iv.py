#
# @lc app=leetcode.cn id=1510 lang=python3
#
# [1510] 石子游戏 IV
#

# @lc code=start
cheattable = []
for i in range(1, 1000):
    t = i*i
    if t > 100000:
        break
    cheattable.append(t)
# dp = [False]
# for i in range(1, 100001):
#     dp.append(False)
#     for coin in cheattable:
#         if coin > i:
#             break
        
#         if not dp[i - coin]:
#             dp[-1] = True
#             break
'''
大表速度没有小表快
'''
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False]
        for i in range(1, n+1):
            dp.append(False)
            for coin in cheattable:
                if coin > i:
                    break
                
                if not dp[i - coin]:
                    dp[-1] = True
                    break
        return dp[-1]
# @lc code=end

