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
    
    ST表 稀疏表
    二分地存祖先，找的时候二分地向上找
    '''
    def __init__(self, n: int, parent: List[int]):
        '''
        50000要16位
        '''
        carry  = n.bit_length() - 1
        self.dp = [[parent[i]] + [-1] * carry for i in range(n)]
        
        for j in range(1, carry+1):
            for i in range(n): # 别的节点的前面的祖先可能还没找到，得控制所有节点一起往后维护
                if self.dp[i][j-1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        hop = k.bit_length()-1
        while hop >= 0 and node != -1:
            if (k >> hop) & 1:
                node = self.dp[node][hop]
            hop -= 1
        return node
# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
# @lc code=end