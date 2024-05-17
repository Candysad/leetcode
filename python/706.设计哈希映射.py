#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#
from bisect import *
# @lc code=start
class MyHashMap:

    def __init__(self):
        self.table = [[] for _ in range(1000)]


    def put(self, key: int, value: int) -> None:
        khash = key % 1000
        if self.table[khash]:
            index = bisect_left(self.table[khash], key, key=lambda x:x[0])
            if index == len(self.table[khash]):
                self.table[khash].append([key, value])
                
            elif self.table[khash][index][0] == key:
                self.table[khash][index][1] = value

            else:
                self.table[khash].insert(index, [key, value])
        else:
            self.table[khash].append([key, value])


    def get(self, key: int) -> int:
        khash = key % 1000
        if self.table[khash]:
            index = bisect_left(self.table[khash], key, key=lambda x:x[0])
            if index == len(self.table[khash]):
                return -1
            elif self.table[khash][index][0] == key:
                return self.table[khash][index][1]
        return -1
                
                
    def remove(self, key: int) -> None:
        khash = key % 1000
        if self.table[khash]:
            index = bisect_left(self.table[khash], key, key=lambda x:x[0])
            if index == len(self.table[khash]):
                return
            elif self.table[khash][index][0] == key:
                self.table[khash].remove(self.table[khash][index])

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

