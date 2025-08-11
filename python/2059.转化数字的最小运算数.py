#
# @lc app=leetcode.cn id=2059 lang=python3
#
# [2059] 转化数字的最小运算数
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        queue = [start]
        layer = 0
        vis = set([start])
        while queue:
            t = queue
            queue = []
            for node in t:
                for num in nums:
                    for t in [node + num, node-num, node ^ num]:
                        if t not in vis:
                            vis.add(t)
                            if t == goal: return layer + 1
                            if 0 <= t <= 1000:
                                queue.append(t)
            layer += 1
        return -1
# @lc code=end