#
# @lc app=leetcode.cn id=1997 lang=python3
#
# [1997] 访问完所有房间的第一天
#
from collections import Counter
# @lc code=start
mod = 10**9 + 7
class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        '''
        动态规划
        nexti <= i
        到i
            从i到i（这一次跳之前i是奇数次，最少访问1次）
            从i-1到i，i-1访问了偶数次
        所以要增长必须由i-1跳过来，且i-1已经至少访问过2次
        
        对于最早到达i的第dp[i]天
            从i过来 不是最早 
            从i-1过来，即 偶数次访问i-1的时间 + 1 = dp[i]
            nextVisit 会导致回退，每次回退会增加时间
        回退一次到 j,j < i
            此时奇数次到 j，则需要再回退
                直到出现一个偶数次位置才靠近一次
                必须路上全是偶数次才会到达i
            此时是偶数次，则增长靠近i
            对于到达i，一定是路上都是偶数次来的
            一旦从 i 回退到 j，j 此时就是奇数次，需要从j开始重复一遍【第一次到j然后到i】的过程
            dp[x] 为从0第一次到x的时间
            则第一次从j到i为 dp[i] - dp[j]
        没回退就在 i，则继续增长
        
        dp[i] 为第一次到i的时间
        '''
        n = len(nextVisit)
        dp = [0] * n
        for i in range(1, n):
            # dp[i] = dp[i-1] + (dp[i-1] - dp[nextVisit[i-1]] + 1) + 1
            dp[i] = (2 * dp[i-1] - dp[nextVisit[i-1]] + 2) % mod
        return dp[-1]   
        '''
        模拟
        超时..😓
        '''
        # counter = Counter()
        # n = len(nextVisit)
        # counter[0] = 1
        # nowi = nextVisit[0]
        # result = 0
        # while len(counter) != n:
        #     result = (result + 1) % mod
        #     counter[nowi] += 1
        #     if counter[nowi] % 2:
        #         nowi = nextVisit[nowi] 
        #     else:
        #         nowi += 1

        # return result
# @lc code=end

