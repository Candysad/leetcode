#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除并获得点数
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        '''
        转成 198.打家劫舍
        两次O(n)遍历，时间复杂度O(n),
        空间复杂度其实最大为 O(4000), 即 O(n)
        '''
        f = [0 for _ in range(max(nums))] # 控制下最大位置减少时间
        for n in nums: # 把重复数量按数字量转为待偷的房子，没出现的房子相当于没钱
            f[n-1] += n
        
        left = right = 0
        for n in f:
            left, right = right, max(left+n, right)
        return right
        
# @lc code=end

