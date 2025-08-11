#
# @lc app=leetcode.cn id=1559 lang=python3
#
# [1559] 二维网格图中探测环
#

# @lc code=start
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        tree = [i for i in range(m*n)]
        
        def find(node):
            while node != tree[node]:
                node = tree[node]
            return node
        
        def merge(node1, node2):
            head1, head2 = find(node1), find(node2)
            if head1 == head2: return True
            if head1 > head2:
                head1, head2 = head2, head1
            tree[node1], tree[node2], tree[head2] = head1, head1, head1
            return False
        
        for i in range(m):
            for j in range(n):
                node = i * n + j
                if i > 0 and grid[i-1][j] == grid[i][j]:
                    if merge(node, (i - 1) * n + j): return True
                
                if j > 0 and grid[i][j-1] == grid[i][j]:
                    if merge(node, i * n + j - 1): return True
        return False
# @lc code=end