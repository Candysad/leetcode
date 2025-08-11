#
# @lc app=leetcode.cn id=419 lang=python3
#
# [419] 甲板上的战舰
#

# @lc code=start
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        
        tree = [i for i in range(m*n)]
        
        def find(node):
            while node != tree[node]:
                node = tree[node]
            return node
        
        def merge(node1, node2):
            head1, head2 = find(node1), find(node2)
            if head1 == head2: return
            if head1 > head2:
                head1, head2 = head2, head1
                node1, node2 = node2, node1
            
            tree[node1], tree[node2], tree[head2] = head1, head1, head1
        
        def optimize():
            result = set()
            for i in range(m):
                for j in range(n):
                    node = i * n + j
                    if board[i][j] == 'X':
                        result.add(tree[node])
            return len(result)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    node = i * n + j
                    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if 0 <= x < m and 0 <= y < n and board[x][y] == 'X':
                            merge(x*n + y, node)
        
        return optimize()
# @lc code=end