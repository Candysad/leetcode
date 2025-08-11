#
# @lc app=leetcode.cn id=2908 lang=python3
#
# [2908] 元素和最小的山形三元组 I
#
from heapq import *
# @lc code=start
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        '''
        左右分别一个优先队列
            左边随遍历过程添加元素，但其实也不用优先队列，就每次单独比较最新的最小值就好
            右边懒更新，堆顶元素的下标小于等于当前遍历位置就弹出去丢掉
            其实不好
            懒更新是为了弥补优先队列内部不能访问的问题
        '''
        n = len(nums)
        leftmin = nums[0]
        rightmins = [(nums[i], i) for i in range(1,n)]
        heapify(rightmins)
        
        result = 151
        for i in range(1, n-1):
            leftmin = min(leftmin, nums[i-1])
            while rightmins[0][1] <= i:
                heappop(rightmins)
            
            rightmin = rightmins[0][0]
            if leftmin < nums[i] > rightmin:
                result = min(result, leftmin + nums[i] + rightmin)
            
        return result if result != 151 else -1
        
        '''
        左右两边分别记录 [0...i] 和 [i...n-1] 之间的最小值
        然后遍历1...n-1，找这个数和两侧最小值的和，记录和的最小值
        左侧的遍历可以和中间放在同一次里
        '''
        # n = len(nums)
        # leftmins = []
        # t_min = nums[0]
        # for i in range(n-2):
        #     t_min = min(t_min, nums[i])
        #     leftmins.append(t_min)
        
        # t_min = nums[-1]
        # rightmins = []
        # for i in range(n-1, 1, -1):
        #     t_min = min(t_min, nums[i])
        #     rightmins.append(t_min)
            
        # result = 151
        # for i in range(1, n-1):
        #     if nums[i] > leftmins[i-1] and nums[i] > rightmins[n-i-2]:
        #         result = min(result, nums[i] + leftmins[i-1] + rightmins[n-i-2])
        
        # return result if result != 151 else -1
# @lc code=end

