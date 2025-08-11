#
# @lc app=leetcode.cn id=1971 lang=python3
#
# [1971] 寻找图中是否存在路径
#

# @lc code=start
'''
并查集
检查连通性
'''
def find(woods:List, node:int):
    # 找一颗树的根节点
    while woods[node] != node:
        node = woods[node]
    return node

def merge(woods:List, node1:int, node2:int):
    # 找两棵树的根，把更小的作为新的根
    root1 = find(woods, node1)
    root2 = find(woods, node2)
    if root1 < root2:
        woods[root2] = root1
    else:
        woods[root1] = root2

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        woods = [i for i in range(n)]
        for e in edges:
            merge(woods, e[0], e[1])
        
        # print(woods)
        # print([i for i in range(n)])
        return find(woods, source) == find(woods, destination)
        
# @lc code=end

