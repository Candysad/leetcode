#
# @lc app=leetcode.cn id=624 lang=python3
#
# [624] 数组列表中的最大距离
#
'''
给定 m 个数组，每个数组都已经按照升序排好序了
现在你需要从两个不同的数组中选择两个整数（每个数组选一个）并且计算它们的距离
两个整数 a 和 b 之间的距离定义为它们差的绝对值 |a-b| 
你的任务就是去找到最大距离

示例
输入： 
[
    [1,2,3],
    [4,5],
    [1,2,3]
]
输出： 4
解释：
一种得到答案 4 的方法是从第一个数组或者第三个数组中选择 1，同时从第二个数组中选择 5 。
'''
# @lc code=start
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m = len(arrays)
        maxs = []
        mins = []

        for i in range(m):
            mn, mx = arrays[i][0], arrays[i][-1]
            mins.append((mn, i))
            maxs.append((-mx, i))
        
        heapify(mins)
        heapify(maxs)

        max1, max1i = heappop(maxs)
        max1 = - max1
        min1, min1i = heappop(mins)
        if max1i != min1i:
            return max1 - min1

        max2, max2i = heappop(maxs)
        max2 = - max2
        min2, min2i = heappop(mins)
        return max(max2 - min1, max1 - min2)
# @lc code=end

