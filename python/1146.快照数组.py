#
# @lc app=leetcode.cn id=1146 lang=python3
#
# [1146] 快照数组
#
from bisect import *
# @lc code=start
class SnapshotArray:

    def __init__(self, length: int):
        self.arraries = [[[0, 0]] for _ in range(length)]
        self.version = 0

    def set(self, index: int, val: int) -> None:
        if self.arraries[index][-1][1] == self.version:
            self.arraries[index][-1][0] = val
        else:
            self.arraries[index].append([val, self.version])

    def snap(self) -> int:
        self.version += 1
        return self.version - 1

    def get(self, index: int, snap_id: int) -> int:
        t_queue = self.arraries[index]
        i = bisect_left(t_queue, snap_id, key=lambda x:x[1])
        
        if i == len(self.arraries[index]):
            return self.arraries[index][-1][0]
        
        if self.arraries[index][i][1] == snap_id:
            return self.arraries[index][i][0]

        return self.arraries[index][i-1][0]
# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end

