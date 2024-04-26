#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
from bisect import bisect_left
# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
            最后的降序部分说明该部分已经变成最大了
            离开降序的第一个数 2 311 即 2，需要被换进降序部分
            为了使换进去之后变大，换出来到2的位置上的需要比2大，且是刚好大一点的
            2 换进去之后，2左侧的比换出来的数3更大，也同样比2大；2右侧的数小于3，则也应该小于等于2
            即换进去之后，降序部分仍然保持降序，此时字典序因为3换出去已经变大了，可以把降序部分反过来变小，使得从3开始的部分字典序最小
    
            总要有至少一个降序
            全是降序则直接反过来回到最开头
        '''
        # 找降序部分
        i = len(nums)-1
        if i == 0:
            return nums
        
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        
        if i == 0:
            nums[:] = nums[::-1]
            return

        # 找到要换进去的位置
        left = i-1
        # 找换出来的位置
        right = bisect_left(nums[i:], -nums[left], key=lambda x:-x) + i-1 # 二分查找-1是目标坐标，但是nums截取了右侧，坐标还要从i开始，所以是 -1 + i
        
        # print("left", left, nums[left])
        # print("right", right, nums[right])
        
        # 交换
        nums[left], nums[right] = nums[right], nums[left]
        # print(nums)
        
        # 降序部分翻转成升序
        # print(nums[i:], nums[i:][::-1])
        nums[i:] = nums[i:][::-1]
# @lc code=end

