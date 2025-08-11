#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#
from bisect import bisect_left
from collections import Counter
from math import inf
# @lc code=start
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        
        keys = [-inf] + sorted(list(counter.keys())) # 开头哨兵用来处理第一个前缀为 0
        
        N = len(keys)
        fens = [0] * N # fens 有效长度就是有效元素长度，实际长度考虑开头有没有哨兵以及从1开始跳过0
        def lowerbit(i):
            return i & -i

        def get(i):
            result = 0
            while i:
                result += fens[i]
                i -= lowerbit(i)
            return result

        def update(i, delta=1):
            while i < len(fens):
                fens[i] += delta
                i += lowerbit(i)
            
        result = []
        for num in nums[::-1]:
            i = bisect_left(keys, num)
            result.append(get(i))
            update(i+1)
        return result[::-1]


        '''
        二分直接插进去找
        '''
        # post = []
        # result = []
        
        # for num in nums[::-1]:
        #     i = bisect_left(post, num)
        #     result.append(i)
        #     post.insert(i, num)
        
        # return result[::-1]
        
        
# @lc code=end

