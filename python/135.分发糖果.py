#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''
        左右两个方向两次遍历
        '''
        n = len(ratings)
        result = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                result[i] = result[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1] and result[i+1]+1 > result[i]:
                result[i] = result[i+1] + 1
        
        return sum(result)
            
            
        
        
        '''
        广度优先
        '''
        # n = len(ratings)
        # result = [1] * n
        # queue = []
        # if n >= 2:
        #     if ratings[0] < ratings[1]:
        #         queue.append([1, 1, 2])
        #     if ratings[-1] < ratings[-2]:
        #         queue.append([n-2, -1, 2])
            
        # for i, r in enumerate(ratings[1:-1]):
        #     if ratings[i-1] <= ratings[i] <= ratings[i+1]:
        #         if ratings[i-1] > ratings[i]:
        #             queue.append([i-1, -1, 2])

        #         if ratings[i+1] > ratings[i]:
        #             queue.append([i+1,  1, 2])
        
        # while queue:
        #     t = queue
        #     queue = []
        #     for i, direct, num in t:
        #         if result[i] < num:
        #             result[i] = num
        #         if 0 <= i + direct < n:
        #             if ratings[i+direct] > ratings[i]:
        #                 queue.append([i+direct, direct, result[i]+1])
        
        # mincandy = min(result)
        # return sum(result) - n*(mincandy-1)
# @lc code=end

