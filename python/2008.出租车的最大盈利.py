#
# @lc app=leetcode.cn id=2008 lang=python3
#
# [2008] 出租车的最大盈利
#
from collections import defaultdict
# @lc code=start
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        table = set()
        for i, j, _ in rides:
            table.add(i)
            table.add(j)
        table = sorted(list(table))
        n = len(table)
        t = zip(range(1, n+1), table)
        table = {k : v for v, k in t}
        
        tree = defaultdict(int)
        def lowerbit(i):
            return i & (-i)

        def update(i, d):
            while i <= n:
                d = max(tree[i], d)
                tree[i] = d
                i += lowerbit(i)
        
        def find(i):
            result = 0
            while i:
                result = max(result, tree[i])
                i -= lowerbit(i)
            return result

        rides.sort()
        for left, right, tip in rides:
            pre = find(table[left])
            update(table[right], pre + tip + right - left)
        
        return find(n)
# @lc code=end