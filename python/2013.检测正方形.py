#
# @lc app=leetcode.cn id=2013 lang=python3
#
# [2013] 检测正方形
#
from collections import defaultdict
# @lc code=start
class DetectSquares:
    def __init__(self):
        self.g = defaultdict(lambda : defaultdict(int))
        self.index = set()
        
    def add(self, point: List[int]) -> None:
        x, y = point
        self.index.add(x)
        self.g[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        result = 0
        for i in self.index:
            if i == x: continue
            
            # 两侧两种情况
            # 左侧对角
            leftcross = (i, y - (x-i))
            pcross = self.g[i][leftcross[1]]
            if pcross:
                # 另外两个点
                p1 = self.g[x][leftcross[1]]
                p2 = self.g[leftcross[0]][y]
                result += p1 * p2 * pcross
            
            # 右侧对角
            rightcross = (i, y + (x-i))
            pcross = self.g[i][rightcross[1]]
            if pcross:
                p1 = self.g[x][rightcross[1]]
                p2 = self.g[rightcross[0]][y]
                result += p1 * p2 * pcross
        return result
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @lc code=end