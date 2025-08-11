#
# @lc app=leetcode.cn id=2009 lang=python3
#
# [2009] 使数组连续的最少操作数
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        # 去重，记录重复的个数，它们都要被改掉
        nums = set(nums)
        n_norepeat = len(nums)
        
        # 排序
        nums = list(nums)
        nums.sort()
        
        # 找本来就能装最多数字的区间
        span_max_count = 0 # 记最多的个数
        left = nums[0]
        right = left + n - 1
        
        max_i = 0 # 在nums里指着下一个要判断的数的下标
        while max_i < n_norepeat and right >= nums[max_i] >= left:
            span_max_count += 1
            max_i += 1
        
        min_i = 0
        span_count = span_max_count # 只需要记最多框住几个数，不需要记框住的是谁
        '''
        线性时间但是全遍历也超时
        
            right += 1 # 区间每次只往右边挪一下
            left += 1
            if nums[min_i] < left:
                span_count -= 1
                min_i += 1
            
            if nums[max_i] <= right:
                span_count += 1
                if span_count > span_max_count:
                    span_max_count = span_count
                max_i += 1
        
        要改成按实际数字移动窗口，每一次移动就一定有新的数进来，不会出现什么都没发生的窗口
        '''
        while max_i < n_norepeat and right <= nums[-1]:
            right = nums[max_i] # 区间最大数直接到下一个数字的位置，+1+1过来的话中间会有空的位置，浪费时间了
            max_i += 1 
            span_count += 1
            left = right - n + 1
            
            while nums[min_i] < left: # 把左边小了的部分丢掉
                span_count -= 1
                min_i += 1
                
            if span_count > span_max_count: # 记录最能框数字的区间框了多少
                span_max_count = span_count
        
        return n - span_max_count
        '''
        其实应该是 
        重复数字一定要改 repeat
        不在区间里的要改 n_norepeat - span_max_count
        最大区间里的不用改 span_max_count
        要改的次数 = repeat + n_norepeat - span_max_count
                   = (repeat + n_norepeat) - span_max_count
                   = n - span_max_count
        '''
# @lc code=end

