#
# @lc app=leetcode.cn id=1519 lang=python3
#
# [1519] 子树中标签相同的节点数
#
from collections import Counter, defaultdict
# @lc code=start
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = defaultdict(list)
        
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        result = [0] * n
        def dfs(a, pre):
            label = labels[a]
            counter = Counter()
            counter[label] += 1
            for b in g[a]:
                if b != pre:
                    t = dfs(b, a)
                    counter.update(t)
            result[a] = counter[label]
            return counter

        dfs(0, n+1)
        return result
# @lc code=end