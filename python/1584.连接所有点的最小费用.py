#
# @lc app=leetcode.cn id=1584 lang=python3
#
# [1584] 连接所有点的最小费用
#
from collections import defaultdict
from math import inf
# @lc code=start
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1: return 0
        queue = []
        for i in range(n):
            for j in range(i+1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                queue.append((d, i, j))
        queue.sort(key=lambda x: x[0])
                
        tree = list(range(n))
        def find(node):
            while node != tree[node]:
                node = tree[node]
            return node
        
        def merge(node1, node2):
            head1, head2 = find(node1), find(node2)
            if head1 == head2: return False
            if head1 > head2:
                head1, head2 = head2, head1
            
            tree[node1], tree[node2], tree[head2] = head1, head1, head1
            return True
        
        result = 0
        for d, i, j in queue:
            if merge(i, j):
                result += d
        
        return result
# @lc code=end