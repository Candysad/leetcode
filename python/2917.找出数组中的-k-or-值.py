#
# @lc app=leetcode.cn id=2917 lang=python3
#
# [2917] 找出数组中的 K-or 值
#

# @lc code=start
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        '''
        位运算数学题
        '''
        ans = 0
        for i in range(32):
            cnt = 0
            for num in nums:
                cnt += (num >> i) & 1  ## 
                if cnt >= k:
                    ans += 1 << i
                    break
        return ans
    
        length = len(nums)
        result = 0
        if k == 1:
            for n in nums:
                result |= n
            return  result
        elif k == length:
            result = nums[0]
            for n in nums:
                result &= n
            return result
        
        for i in range(32):
            t_count = 0
            for j in range(length):
                t_count += nums[j] % 2
                nums[j] >>= 1
            if t_count >= k:
                result += (1 << i)
        return result
# @lc code=end

