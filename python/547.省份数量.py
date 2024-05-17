#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
class Tree:
    def __init__(self, n:int) -> None:
        self.tree = [i for i in range(n)]
        self.count = n
    
    def find(self, node) -> None:
        while node != self.tree[node]:
            node = self.tree[node]
        return node
    
    def merge(self, node1, node2) -> None:
        head1, head2 = self.find(node1), self.find(node2)
        if head1 > head2:
            head1, head2 = head2, head1
        
        if head1 < head2:
            self.tree[head2] = head1
            self.count -= 1
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        tree = Tree(n)
        
        for i in range(n-1):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    tree.merge(i, j)
        return tree.count
# @lc code=end

