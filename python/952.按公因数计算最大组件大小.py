#
# @lc app=leetcode.cn id=952 lang=python3
#
# [952] 按公因数计算最大组件大小
#
from collections import defaultdict
from functools import cache
from math import inf
# @lc code=start
class Solution:     
    def largestComponentSize(self, nums: List[int]) -> int:
        '''
        在筛的时候顺便把并查集一起维护了
        '''
        n = max(nums)+1
        nums = set(nums)
        
        # 并查集
        tree = {}
        size = defaultdict(int)
        def find(node):
            while node != tree[node]:
                node = tree[node]
            return node
        def merge(node1, node2):
            head1, head2 = find(node1), find(node2)
            if head1 == head2:
                return
            tree[head2] = head1
            size[head1] += size[head2]
        
        # 线性筛
        not_pri = [False] * (n+1)
        lastpri = {}
        for i in range(2, n):
            if not not_pri[i]:
                tree[i] = i
                # 以质数为节点
                if i in nums: # 从小到大遍历的，第一次遇见一个 nums 里的就+1
                    size[i] += 1
                
                for j in range(2, n//i + 1):
                    t = i * j
                    not_pri[t] = True
                    # 找质数 i 的倍数
                    if t in nums: # 这个倍数也是 nums 里的
                        if t in lastpri: # 之前出现过，则将之前更小的质数和当前更大的质数在并查集上连起来
                            merge(lastpri[t], i)
                        else: # 之前没出现过，第一次出现给质数 i 的并查集size + 1
                            head = find(i)
                            size[head] += 1
                        lastpri[t] = i # 当前质数 i 就是这个数里的最小质因数

        return max(size.values())
# @lc code=end