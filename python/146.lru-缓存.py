#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
'''
用hash快速查找
用双向链表来确保按照频率更新位置
单次查和更新都是 O(1)
'''
class Node: # 双向链表
    def __init__(self, key:int=-1, val:int=-1, next=None, last=None):
        self.key = key
        self.val = val
        self.next= self if next is None else next
        self.last= self if last is None else last
    
    def __str__(self) -> str:
        return f"{self.key}->{self.next.key if self is not None else None}"

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity # 容量
        self.count = 0           # 当前个数
        self.table = {}          # hash表
        self.head = Node(-1, -1) # 虚空头节点
        self.head.next = None
        # self.last = Node(-1, -1) # 虚空尾节点
        # self.last.last = None


    def get(self, key: int) -> int:
        # 空的不用找
        if self.count == 0:
            return -1
        
        # 看在不在
        node = self.table.get(key, None)
        if node is not None:
            if self.head.next is not node: # 就在开头不用挪
                self.move2head(node)
            return node.val
        else:
            return -1
            
    def put(self, key: int, value: int) -> None:
        # 空的肯定没有，插入新的
        if self.count == 0:
            self.count += 1
            node = Node(key, value)
            self.head.next = node # 放在开头
            self.table[key] = node
            return
        
        node = self.table.get(key, None)
        # 找到了
        if node is not None:
            node.val = value
            if self.head.next is not node:
                self.move2head(node)
            return
        # 没找到，插入新的
        else:
            node = Node(key,value)
            self.table[key] = node
            head = self.head.next
            # 容量够，加在开头
            if self.count < self.capacity:
                self.count += 1
                node.next = head
                node.last = head.last
                
                node.last.next = node
                node.next.last = node
                self.head.next = node
                return
            # 满了，加在开头，然后去掉末尾
            else:
                node.next = head
                node.last = head.last
                
                node.last.next = node
                node.next.last = node
                
                last = node.last
                self.table[last.key] = None
                
                node.last = last.last
                node.last.next = node
                self.head.next = node
                return
    
    def move2head(self, node):
        if self.head.next is node:
            return
        
        head = self.head.next
        
        node.last.next = node.next
        node.next.last = node.last
        
        node.next = head
        node.last = head.last
        
        node.next.last = node
        node.last.next = node
    
        self.head.next = node
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

