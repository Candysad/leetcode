#
# @lc app=leetcode.cn id=1722 lang=python3
#
# [1722] 执行交换操作后的最小汉明距离
#
from collections import defaultdict, Counter
# @lc code=start
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        tree = [i for i in range(n)]
        
        def find(node):
            while node != tree[node]:
                node = tree[node]
            return node
        
        def merge(node1, node2):
            head1, head2 = find(node1), find(node2)
            if head1 == head2: return
            if head1 > head2:
                head1, head2 = head2, head1
            tree[head2], tree[node1], tree[node2] = head1, head1, head1
        
        def opt():
            subsource = defaultdict(Counter)
            subtarget = defaultdict(Counter)
            for i in range(n):
                subsource[find(i)][source[i]] += 1
                subtarget[find(i)][target[i]] += 1
            
            result = 0
            for key in subsource:
                t = 0
                for num in subtarget[key]:
                    t += max(subtarget[key][num] - subsource[key][num], 0)
                result += t
            
            return result

        for a, b in allowedSwaps:
            merge(a ,b)
        
        return opt()    
# @lc code=end