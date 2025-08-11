#
# @lc app=leetcode.cn id=1723 lang=python3
#
# [1723] 完成所有工作的最短时间
#

# @lc code=start
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        status = 1 << n
        table = [0] * status
        for i in range(n):
            now = 1 << i
            for j in range(now):
                table[now | j] = table[j] + jobs[i]
        
        t = table.copy()
        for _ in range(1, k):
            for i in range(status-1, 0, -1):
                now = i
                while now:
                    c = t[i ^ now]
                    if table[now] > c: c = table[now]
                    if c < t[i]: t[i] = c
                    now = (now-1) & i
        return t[-1]
# @lc code=end