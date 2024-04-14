#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#
from bisect import bisect_left
# @lc code=start
class MyHashSet:

    def __init__(self):
        '''
        数组+有序链表
        单次最多1000次查询，乐观考虑放1000个槽位
        hash(key) = key % 1000
        
        发生冲突就递增地放进槽位里形成链表
        用二分查
        '''
        self.table = [[]] * 1000

    def add(self, key: int) -> None:
        slot = key % 1000
        if self.table[slot]:
            t = bisect_left(self.table[slot], key)
            if t >= len(self.table[slot]):
                self.table[slot].append(key)
                return
            if self.table[slot][t] == key:
                return
            
            self.table[slot].insert(t, key)
        else:
            self.table[slot].append(key)
            
    def remove(self, key: int) -> None:
        slot = key % 1000
        if self.table[slot]:
            t = bisect_left(self.table[slot], key)
            if t >= len(self.table[slot]):
                return
            if self.table[slot][t] == key:
                self.table[slot].remove(key)


    def contains(self, key: int) -> bool:
        slot = key % 1000
        if self.table[slot]:
            t = bisect_left(self.table[slot], key)
            if t >= len(self.table[slot]):
                return False
            if self.table[slot][t] == key:
                return True
        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

