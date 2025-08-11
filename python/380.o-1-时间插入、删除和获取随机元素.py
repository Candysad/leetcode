#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#
from random import randint
# @lc code=start
class RandomizedSet:
    '''
    变长数组
    每次删除一个，就把最后面的填在前面，总长缩短 1
    '''
    def __init__(self):
        self.table = {}
        self.arr = []
        self.index = 0

    def insert(self, val: int) -> bool:
        if val not in self.table:
            self.table[val] = self.index
            if self.index == len(self.arr):
                self.arr.append(val)
            else:
                self.arr[self.index] = val
            self.index += 1
            return True
        return False
        
    def remove(self, val: int) -> bool:
        if val in self.table:
            index = self.table[val]
            self.arr[index] = self.arr[self.index-1]
            self.table[self.arr[self.index-1]] = index
            self.index -= 1
            del self.table[val]
            return True
        return False


    def getRandom(self) -> int:
        index = randint(0, self.index-1)
        return self.arr[index]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

