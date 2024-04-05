#
# @lc app=leetcode.cn id=1483 lang=python3
#
# [1483] 树节点的第 K 个祖先
#

# @lc code=start
class TreeAncestor:
    '''
    直接用并查集查会超时...😓
    不是，那我先查出来存着查的过程时间复杂度不是更高么
    
    用别的数据结构增加冗余信息来提升查的速度只会让空间爆炸
    只在长兄存祖先信息也会内存爆炸啊...😥
    
    
    '''
    def __init__(self, n: int, parent: List[int]):
        self.ancestor = [[], -1] * n
        self.ancestor[0] = [[], -1]
        for i in range(1, n):
            left, right = self.ancestor[parent[i]]
            if right == -1:
                self.ancestor[parent[i]][1] = i
                left = left + [parent[i]]
            else:
                left = self.ancestor[right][0]
            self.ancestor[i] = [left, -1]
        
    def getKthAncestor(self, node: int, k: int) -> int:
        ancestor = self.ancestor[node][0]
        if len(ancestor) < k:
            return -1
        return ancestor[-k]

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
# @lc code=end

