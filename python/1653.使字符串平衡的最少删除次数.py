#
# @lc app=leetcode.cn id=1653 lang=python3
#
# [1653] 使字符串平衡的最少删除次数
#

# @lc code=start
class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp0, dp1 = 0, 0 # 上一个是 a 的平衡代价， 上一个是 b 的
        for c in s:
            if c == 'a':
                t0, t1 = dp0, dp1 + 1
            else:
                t0, t1 = dp0 + 1, min(dp0, dp1)
            dp0, dp1 = t0, t1
        return min(dp0, dp1)  
# @lc code=end

