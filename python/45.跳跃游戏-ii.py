#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        题目保证可以到达
        '''
        n = len(nums)
        if n == 1:
            return 0
        
        left = 1
        right = nums[0]
        step = 1
        
        while right < n-1:
            t = right # 第 step 次最远能到的地方
            while left <= right: # 从left开始一直到right都是第 step - 1次可能的启动
                t = max(t, left + nums[left])
                left += 1
            right = t
            step += 1
            
        return step

# @lc code=end

