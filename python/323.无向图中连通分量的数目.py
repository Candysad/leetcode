#
# @lc app=leetcode.cn id=323 lang=python3
#
# [323] 无向图中连通分量的数目
#

# @lc code=start
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        tree = [i for i in range(n)]
        
        def find(node):
            while node != tree[node]:
                node = tree[node]
            return node
        
        def merge(node1, node2):
            head1, head2 = find(node1), find(node2)
            if head1 == head2: return
            if head2 < head1:
                head1, head2 = head2, head1
            tree[head2], tree[node1], tree[node2] = head1, head1, head1
        
        def opt():
            table = set()
            for i in range(n):
                table.add(find(i))
            return len(table)

        for a, b in edges:
            merge(a, b)
        
        return opt()
# @lc code=end