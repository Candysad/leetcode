#
# @lc app=leetcode.cn id=1202 lang=python3
#
# [1202] 交换字符串中的元素
#
from collections import defaultdict
# @lc code=start
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        tree = [i for i in range(n)]
        
        def find(node):
            while tree[node] != node:
                node = tree[node]
            return node

        def merge(node1, node2):
            head1, head2 = find(node1), find(node2)
            if head1 == head2: return
            if head2 > head1:
                head1, head2 = head2, head1
            
            tree[node1], tree[node2], tree[head2] = head1, head1, head1
        
        def opt():
            result = [0] * n
            trees = defaultdict(list)
            treec = defaultdict(list)
            
            for node in range(n):
                head = find(node)
                trees[head].append(node)
                treec[head].append(s[node])
            
            for head in trees:
                treec[head].sort()
                for i, index in enumerate(trees[head]):
                    result[index] = treec[head][i]
            
            return ''.join(result)

        for a, b in pairs:
            merge(a, b)
        return opt()
# @lc code=end