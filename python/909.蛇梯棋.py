#
# @lc app=leetcode.cn id=909 lang=python3
#
# [909] 蛇梯棋
#

# @lc code=start
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        ntoi = {}
        iton = {}
        n = len(board)
        sign = 0
        now = 1
        for i in range(n-1, -1, -1):
            if sign == 0:
                for j in range(n):
                    ntoi[now] = (i, j)
                    iton[(i, j)] = now
                    now += 1
                sign = 1
            else:
                for j in range(n-1, -1, -1):
                    ntoi[now] = (i, j)
                    iton[(i, j)] = now
                    now += 1
                sign = 0
        
        queue = [1]
        vis = set()
        layer = 0
        while queue:
            t = queue
            queue = set()
            for node in t:
                if node == n*n:return layer
                if node not in vis: vis.add(node)
                
                for nextnode in range(node+1, min(node+6, n*n)+1):
                    x, y = ntoi[(nextnode)]
                    if board[x][y] != -1:
                        if board[x][y] not in vis:
                            nextnode = board[x][y]
                            queue.add(nextnode)
                    elif nextnode not in vis:
                        queue.add(nextnode)
            layer += 1
            queue = list(queue)
        
        return -1
# @lc code=end