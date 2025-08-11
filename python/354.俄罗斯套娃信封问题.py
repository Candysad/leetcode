#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#
from bisect import bisect_left
# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        '''
        二维的递增子序列
        只找最长的长度
        
        先控制住一边增长（排序）
        另一边去比较
        不是等差序列，不能用counter
        出现次序也无所谓，只看大小
        O(n^2) 复杂度遍历，从前往后找每个信封最大能装的
        即使用分组桶也不能确定最后面的桶里有最长的末尾，复杂度还是高
        
        先排序，宽度从小到大，高度从大到小
        有新的末尾就延长，当前长度有新的更小的可行的边就更新
        每个信封都尝试在队列里找自己能放下去的位置，二分查找则复杂度和排序保持一致
        因为先排序可以确保
            后面更宽的一定出现在自己后面
            相同宽度的后面的一定比自己高度小
        每一轮看相同宽度的
            更新高度位置，后续更宽的一定比当前宽，一定可以继续更新
            更新宽度位置，之前的一定比当前宽度小，一定可以继续更新
        '''
        if len(envelopes) == 0:
            return 0
        
        envelopes.sort(key=lambda x : (x[0], -x[1])) # 宽度从小到大，高度从大到小
        d = [envelopes[0][1]]
        
        for e in envelopes[1:]:
            height = e[1]
            if height > d[-1]:
                d.append(height)
            else:
                index = bisect_left(d, height) # 二分查找
                d[index] = height
        
        return len(d)
# @lc code=end

