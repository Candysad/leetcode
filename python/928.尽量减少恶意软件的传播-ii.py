#
# @lc app=leetcode.cn id=928 lang=python3
#
# [928] 尽量减少恶意软件的传播 II
#

# @lc code=start
def find(union, node):
    while union[node] != node:
        node = union[node]
    return node

def merge(union, node1, node2):
    head1 = find(union, node1)
    head2 = find(union, node2)
    if head1 > head2:
        head1, head2 = head2, head1
    
    union[head2] = head1

def optimize(union):
    for i in range(len(union)):
        union[i] = find(union, i)

class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        '''
        先并查集确定不感染的子集（森林里的树）
        再找每个初始感染节点可以感染的子集
        再反过来找每个子集会被感染的来源
        来源只有一个的，把那个初始感染节点删了就好了
        有不止一个的，删哪个都没用
        
        最后遍历初始感染节点和子集的感染来源，找每个初始感染节点移除后可以减少的总数
        并查集的意义是实现传播，不然间接传播太难找了
        '''
        n = len(graph)
        union = [i for i in range(n)]
        initial = set(initial)
        
        # 将初始未感染的子树找出
        for i in range(n):
            if i in initial:
                continue
            for j in range(n):
                if j in initial:
                    continue
                if graph[i][j]:
                    merge(union, i, j)
        optimize(union)
        
        # 存每棵树的大小并初始化感染来源记录
        trees = {} 
        for i in range(n):
            if i not in initial:
                tree = union[i]
                if tree not in trees:
                    trees[tree] = [1, set()]
                else:
                    trees[tree][0] += 1
        
        # 记录感染来源
        for poison in initial:
            for i in range(n):
                if i in initial or graph[poison][i] == 0:
                    continue
                
                trees[union[i]][1].add(poison)
        
        # 找答案
        result = min(initial)
        max_size = 0
        
        for poison in initial:
            size = 0
            for tree in trees.values():
                if len(tree[1]) == 1 and poison in tree[1]:
                    size += tree[0]
            print(poison, size)
            if size > max_size:
                result = poison
                max_size = size
            if size == max_size and poison < result:
                result = poison
                max_size = size
            print(result)
        
        print(initial)
        print(union)
        print(trees)
        
        return result 
# @lc code=end

