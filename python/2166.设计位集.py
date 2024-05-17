#
# @lc app=leetcode.cn id=2166 lang=python3
#
# [2166] 设计位集
#

# @lc code=start
class Bitset:
    def __init__(self, size: int):
        self.size = size
        self.num = [0] * size
        self.ones = 0
        self.f = False

    def fix(self, idx: int) -> None:
        t = self.num[idx] if not self.f else 1 ^ self.num[idx]
        if t == 0:
            self.ones += 1
            self.num[idx] = 0 if self.f else 1
  
    def unfix(self, idx: int) -> None:
        t = self.num[idx] if not self.f else 1 ^ self.num[idx]
        if t == 1:
            self.ones -= 1
            self.num[idx] = 1 if self.f else 0

    def flip(self) -> None:
        self.f = not self.f
        self.ones = self.size - self.ones

    def all(self) -> bool:
        return self.size == self.ones

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones
    
    def toString(self) -> str:
        if not self.f:
            return ''.join( [ str(n) for n in self.num ] )
        else:
            return ''.join( [ str(n^1) for n in self.num ] )
        

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
# @lc code=end