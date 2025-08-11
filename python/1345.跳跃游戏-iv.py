#
# @lc app=leetcode.cn id=1345 lang=python3
#
# [1345] 跳跃游戏 IV
#
from collections import defaultdict
# @lc code=start
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        '''
        根据条件设置两种vis的广度优先
        '''
        n = len(arr)
        table = defaultdict(list)
        for i, num in enumerate(arr):
            table[num].append(i)
        
        vis = set()
        vis.add(n-1)
        numvis = set()
        queue = [n-1]
        layer = 0
        while True:
            t = queue
            queue = []
            for node in t:
                if node == 0:
                    return layer

                if 0 <= node - 1 < n and node-1 not in vis:
                    queue.append(node-1)
                    vis.add(node-1)
                if 0 <= node + 1 < n and node+1 not in vis:
                    queue.append(node+1)
                    vis.add(node+1)

                if arr[node] not in numvis: 
                    for node2 in table[arr[node]]:
                        if node2 not in vis:
                            queue.append(node2)
                            vis.add(node2)
                            numvis.add(arr[node2])
            layer += 1
# @lc code=end