#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#

# @lc code=start
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def encode(board):
            count = 0
            result = 0
            zeroi = -1
            for i in range(2):
                for j in range(3):
                    if board[i][j] == 0: zeroi = count
                    result += board[i][j] * (10 ** count)
                    count += 1    
            return result, zeroi
        
        def move(num, i):
            n1, n2, n3, n4= -1, -1, -1, -1
            result1, result2, result3, result4 = -1, -1, -1, -1
            c = 0
            t = num
            while t:
                # 上下左右
                if c == i-1 and i != 3:
                    n1 = t % 10
                if c == i + 1 and i != 2:
                    n2 = t % 10
                if c == i-3:
                    n3 = t % 10
                if c == i+3:
                    n4 = t % 10
                c += 1
                t //= 10
            if n1 != -1:
                result1 = num - n1 * (10**(i-1)) + n1 * (10**i)
            if n2 != -1:
                result2 = num - n2 * (10**(i+1)) + n2 * (10**i)
            if n3 != -1:
                result3 = num - n3 * (10**(i-3)) + n3 * (10**i)
            if n4 != -1:
                result4 = num - n4 * (10**(i+3)) + n4 * (10**i)
                
            return [(result1, i-1), (result2, i+1), (result3, i-3), (result4, i+3)]

        num, i = encode(board)
        vis = set([-1, num])
        queue = [(num, i)]
        layer = 0
        while queue:
            t = queue
            queue = []
            for num, i in t:
                if num == 54321: return layer
                
                tttt = move(num ,i)
                for nxt in tttt:
                    if nxt[0] not in vis:
                        queue.append(nxt)
                        vis.add(nxt[0])
            layer += 1
        return -1
        
        
# @lc code=end