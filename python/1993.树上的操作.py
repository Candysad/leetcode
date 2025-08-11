#
# @lc app=leetcode.cn id=1993 lang=python3
#
# [1993] 树上的操作
#

# @lc code=start
class Node:
    def __init__(self, num:int, parent:int) -> None:
        self.num = num
        self.parent = parent
        self.lockedchildren = set() # 上锁后代
        self.lock = -1 # -1 没锁，>-1 为上锁用户
    
class LockingTree:

    def __init__(self, parent: List[int]):
        self.nodes = [Node(i, p) for i, p in enumerate(parent)]
        self.n = len(parent)

    def lock(self, num: int, user: int) -> bool:
        node = self.nodes[num]
        
        # 是否已上锁
        if node.lock != -1:
            return False
        
        # 上锁，循环上去更新祖先信息
        node.lock = user
        while node.parent != -1:
            node = self.nodes[node.parent]
            node.lockedchildren.add(num)
        return True
        
    def unlock(self, num: int, user: int) -> bool:
        node = self.nodes[num]
        
        # 是否上锁且是同一用户
        if node.lock != user:
            return False
        
        node.lock = -1
        while node.parent != -1:
            node = self.nodes[node.parent]
            node.lockedchildren.remove(num)
        return True

    def upgrade(self, num: int, user: int) -> bool:
        node = self.nodes[num]

        # 是否上锁
        if node.lock != -1: return False
        # 是否有后代上锁
        if not node.lockedchildren: return False
        
        # 是否有祖先上锁
        pnode = node
        while pnode.parent != -1:
            pnode = self.nodes[pnode.parent]
            if pnode.lock != -1: return False
        
        # 解开后代
        t = list(node.lockedchildren)
        for cnode in t:
            self.unlockanyway(cnode)

        # 自己上锁
        self.lock(num, user)
        return True
        
    def unlockanyway(self, num:int):
        # upgrade 时无视 user 强行解锁后代
        node = self.nodes[num]
        
        node.lock = -1
        
        while node.parent != -1:
            node = self.nodes[node.parent]
            node.lockedchildren.remove(num)
# @lc code=end