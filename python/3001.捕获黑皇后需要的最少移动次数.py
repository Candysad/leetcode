#
# @lc app=leetcode.cn id=3001 lang=python3
#
# [3001] 捕获黑皇后需要的最少移动次数
#

# @lc code=start
class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        rook   = (a, b)
        bishop = (c, d)
        queen  = (e, f)
        
        result = 2
        # 对于车
        # 在同一行
        if rook[0] == queen[0]:
            if bishop[0] == rook[0] and  min(rook[1], queen[1]) < bishop[1] < max(rook[1], queen[1]): # 挡住了，2步
                result = 2
            else: result = 1
        # 同一列
        if rook[1] == queen[1]:
            if bishop[1] == rook[1] and  min(rook[0], queen[0]) < bishop[0] < max(rook[0], queen[0]):
                result = 2
            else: result = 1
        
        # 对于主教
        # 在同一斜线
        qdx, qdy = queen[0] - bishop[0], queen[1] - bishop[1]
        if abs(qdx) == abs(qdy):
            # 看车在不在同一斜线
            rdx, rdy = rook[0] - bishop[0], rook[1] - bishop[1]
            if abs(rdx) == abs(rdy):
                # 车夹在中间
                if (qdx > 0) == (rdx > 0) and (qdy > 0) == (rdy > 0): # 同向
                    if abs(rdx) < abs(qdx):
                        result = 2
                    else: result = 1
                else: result = 1
            else: result = 1
        
        # 车不能秒，教士也不能秒
        return result   
# @lc code=end

