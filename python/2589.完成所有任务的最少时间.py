#
# @lc app=leetcode.cn id=2589 lang=python3
#
# [2589] 完成所有任务的最少时间
#
from bisect import bisect_left
from typing import List
# @lc code=start
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        '''
        贪心栈+二分
        栈里只存连续的有效时间点的区间
        '''
        # 区间起点，终点，到区间结束时的总有效时间点个数
        stack = [[-2, -2, 0]]
        tasks.sort(key=lambda x: x[1])
        
        for start, end, d in tasks:
            # 找从哪里开始能影响到当前遍历的 task
            # 因为按 end 排序遍历，当前遍历的 task 一定比前面的区间更晚结束
            # 即栈内从 i 到 -1的区间都在当前遍历的 task 范围内
            i = bisect_left(stack, start, key= lambda x:x[0])
            # 减去已经在当前 task 的区间内的部分
            d -= stack[-1][2] - stack[i-1][2]
            
            # 可能伸到上一个区间里去了，再减去伸进去的部分
            if start <= stack[i-1][1]:
                d -= stack[i-1][1] - start + 1
            
            # 还需要新增时间点
            # 只能向 [0, end] 的范围内加点
            # 可能会在之前区间之间的空隙里加导致区间合并
            if d > 0:
                # 
                while end - stack[-1][1] <= d: # <= 而不是 < 是因为如果区间连起来了还得再向前合并一次
                    prestart, preend, precount = stack.pop()
                    # 现在末尾的区间实际上是 [prestart, end]，只是还没入栈
                    # 对应 while 条件里的stack[-1] 和 end
                    # 计算新区间连起来之后的总需要的点数=需要加的点+被合并进来的区间所需的点
                    d += preend - prestart + 1
                    # 不是precount因为stack[i][2] 指的是到此处的总出现的点的个数
                
                # 当前没入栈的实际上的末尾区间本来是 [prestart, end]，但当末尾区间的 preend 离 end 足够远时
                # 末尾合并出的区间可能太长了，只需要 [end-d+1，end] 这段就够了，相当于只需要这一段里有d个点
                # 此时 d = 所需新加的点数+之前被合并进来的区间所需的点数，因为合并所以要算上之前区间的需求
                stack.append((end-d+1, end, stack[-1][2] + d))
        return stack[-1][2]

        '''
        暴力贪心
        '''
        # table = set()
        # tasks.sort(key=lambda x: (x[1], x[2]))
        
        # for start, end, d in tasks:
        #     for i in range(start, end + 1):
        #         if i in table:
        #             d -= 1
        #             if d == 0:
        #                 break
        #     while d:
        #         if end not in table:
        #             table.add(end)
        #             d -= 1
        #         end -= 1
                
        # return len(table)
# @lc code=end

