#
# @lc app=leetcode.cn id=924 lang=python3
#
# [924] 尽量减少恶意软件的传播
#

# @lc code=start
def find(tree, node):
    while tree[node] != node:
        node = tree[node]
    return node

def merge(tree, node1, node2):
    head1 = find(tree, node1)
    head2 = find(tree, node2)
    if head2 < head1:
        head1, head2 = head2, head1
    tree[head2] = head1
    
def sort_tree(tree, poison):
    n = len(tree)
    result = {}
    for node in range(n):
        head = find(tree, node)
        tree[node] = head
        t = result.get(head, [0, -1])
        
        if node in poison:
            t[1] = node if t[1] == -1 else -2
        result[head] = t
    
    for head in tree: #计算连通区域的大小
        result[head][0] += 1
    
    return result

class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        '''
        并查集
        '''
        n = len(graph)
        tree = [i for i in range(n)]
        for i in range(n-1):
            for j in range(i+1, n):
                if graph[i][j]:
                    merge(tree, i, j)
        
        poison = set(initial)
        result = sort_tree(tree, poison)
        
        max_size = 0
        result_node = n
        for size, node in result.values():
            if node >= 0:
                if size > max_size:
                    result_node = node
                    max_size = size
                if size == max_size and node < result_node:
                    result_node = node
                
        return result_node if result_node != n else min(initial)
# @lc code=end

