#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
#

# @lc code=start
def find(tree, node):
    while tree[node] != node:
        node = tree[node]
    return node

def merge(tree, node1, node2):
    if node1 == node2:
        return
    head1, head2 = find(tree, node1), find(tree, node2)
    if head1 > head2:
        head1, head2 = head2, head1
    
    tree[head2] = head1
    
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = [[] for _ in range(n)]
        for a, b in dislikes:
            g[a-1].append(b-1)
            g[b-1].append(a-1)

        tree = [i for i in range(n)]
        for i in range(n):
            headi = find(tree, i)
            for j in g[i]:
                merge(tree, g[i][0], j)
                if headi == find(tree, j):
                    return False
        return True
# @lc code=end

