#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#
from collections import defaultdict
# @lc code=start
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        table = defaultdict(list)
        
        for b in bank:
            for i in range(8):
                table[b[:i] + '*' + b[i+1:]].append(b)
        
        layer = 0
        queue = [startGene]
        vis = set()
        while queue:
            t = queue
            queue = []
            for node in t:
                for i in range(8):
                    s = node[:i] + '*' + node[i+1:]
                    for nextnode in table[s]:
                        if nextnode != node and nextnode not in vis:
                            if nextnode == endGene: return layer + 1
                            
                            queue.append(nextnode)
                            vis.add(nextnode)

            layer += 1
        
        return -1
# @lc code=end