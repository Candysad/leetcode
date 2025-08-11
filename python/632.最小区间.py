#
# @lc app=leetcode.cn id=632 lang=python3
#
# [632] 最小区间
#
from heapq import *
# @lc code=start
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        '''
        nums 本身有序
        每个数组每次都放一个数字进来，确保当前能至少有一个在里面
        每次最小和最大值决定一个区间
        每次弹出最小的，哪个数组弹出去了就再加一个进来
        '''
        n = len(nums)
        queue = []
        t_max = -100001
        for i in range(n):
            nums[i][:] = nums[i][::-1] # 倒过来方便用 pop
            t_max = max(nums[i][-1], t_max) # 找第一个区间的最大值
            heappush(queue, (nums[i].pop(), i)) # 放入第一个区间的数字
        result = [queue[0][0], t_max] # 第一个区间
        
        while nums[queue[0][1]]: # 如果有某一行已经没数字了就停下
            _, i = heappop(queue) # 弹出当前最小的
            t_max = max(nums[i][-1], t_max) # 加入弹出那一行的下一个数字，确保当前区间最大值
            heappush(queue, (nums[i].pop(), i)) 
            
            span = [queue[0][0], t_max]
            if span[1] - span[0] < result[1] - result[0]:
                result = span
            elif span[1] - span[0] == result[1] - result[0]:
                result = span if span[0] < result[0] else result
            
        return result
# @lc code=end

