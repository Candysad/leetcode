#
# @lc app=leetcode.cn id=1953 lang=python3
#
# [1953] 你可以工作的最大周数
#
from heapq import *
# @lc code=start
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        '''
        n 个一样大的肯定能全部完成
        用最小的减少最大的，形成2个相同大小的最大的
        2个相同大小最大的可以一起减小，变成第3大的，进而大家都变成一样的
        所以只要能出现2个一样的最大值，所有的都能完成
        
        如果不能把最大的变成和第二大的一样大，那就说明不能全部完成
        
        特殊情况：1个或2个数
        
        '''
        n = len(milestones)
        if n == 1:
            return 1
        
        _sum = sum(milestones)
        _max = max(milestones)
        if 2 * _max <= _sum:
            return _sum
        else:
            return 2 * (_sum - _max) + 1

        '''
        优先队列模拟
        肯定超时
        '''
        # queue = []
        # for t in milestones:
        #     heappush(queue, -t)
        
        # result = 0
        # last = None
        # while queue:
        #     top = -heappop(queue)
        #     top -= 1
        #     result += 1
        #     if last is not None:
        #         heappush(queue, -last)
        #     last = top if top else None

        # return result
# @lc code=end

