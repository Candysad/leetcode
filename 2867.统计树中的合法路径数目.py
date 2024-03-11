#
# @lc app=leetcode.cn id=2867 lang=python3
#
# [2867] 统计树中的合法路径数目
#

# @lc code=start
# 埃氏筛
N = 100001
is_prime = [0, 0, 1] + [0 if i % 2 else 1 for i in range(N-3)]
for i in range(2, isqrt(N)+1):
    if is_prime[i]:
        for j in range(i*i, N, i):
            is_prime[j] = 0

'''
用一个列表和一个字典（hash表）来做并查集
列表记录连通的不带质数节点的子树
字典记录每个树上的节点数目
'''
# 并查集
def find(woods:List, node:int):
    while woods[node] != node:
        node = woods[node]
    return node

def merge(woods:List, node1:int, node2:int):
    p1 = find(woods, node1)
    p2 = find(woods, node2)
    if p1 < p2:
        woods[p2] = p1
    else:
        woods[p1] = p2

# 优化并查集并记录子树上的节点个数
def optim(woods:List, node_count:dict):
    for i, node in enumerate(woods):
        woods[i] = find(woods, node)
        node_count[woods[i]] = 0
    for root in woods:
        node_count[root] += 1

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        '''
        埃氏筛
        并查集
        
        用并查集记录连通的非质数子树，并记录树的大小
        遍历质数节点，找它们的非质数邻居所在的子树形成合法路径
        1.质数做端点：子树多大就有多少路径
        2.质数在中间：两侧树的大小相乘，乘法选择
        遍历质数节点并记录已经知道的另一侧路径总数，用作和下一侧相乘
        
        这题给的n，编号从1到n
        能通 但是好像有点慢
        '''
        woods = [i for i in range(n+1)]
        node_count = {}
        grid = [[] for _ in range(n+1)] # 记录节点的相邻节点
        
        # 建立并查集
        for u,v in edges:
            # 记录相邻
            grid[u].append(v)
            grid[v].append(u)
            
            # 加入并查集
            if is_prime[u] or is_prime[v]:
                continue
            merge(woods, u, v)
        # 优化并查集，记录子树大小
        optim(woods, node_count)
        
        result = 0
        for i in range(2, n+1):
            if is_prime[i]:
                t_sum = 0 # 本轮截至目前的所有子树的路径个数和，用于和新子树做乘法组合
                t_result = 0 # 本轮记录的答案总数
                for adjacent in grid[i]:
                    if is_prime[adjacent]:
                        continue
                    
                    now_node_count = node_count[woods[adjacent]]
                    
                    t_result += t_sum * now_node_count      #两侧乘法组合的数目
                    t_result += node_count[woods[adjacent]] # 新值一侧的数目
                    
                    t_sum += now_node_count
                result += t_result
        return result
# @lc code=end

