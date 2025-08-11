#
# @lc app=leetcode.cn id=995 lang=python3
#
# [995] K 连续位的最小翻转次数
#

# @lc code=start
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        flip = 0
        table = set()
        for i in range(n-k+1):
            if i in table:
                table.remove(i)
                flip -= 1
            
            if nums[i] == 0:
                if flip % 2 == 0:
                    flip += 1
                    table.add(i + k)
                    result += 1
            else:
                if flip % 2:
                    flip += 1
                    table.add(i+k)
                    result += 1
            
        for i in range(n-k+1, n):
            if i in table:
                table.remove(i)
                flip -= 1
            
            if nums[i] == 0:
                if flip % 2 == 0:
                    return -1
            
            else:
                if flip % 2:
                    return -1
        
        return result
# @lc code=end