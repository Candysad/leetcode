#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:
    '''
    从前往后维护二维数组存指定位置差
    会爆内存...😓
    '''
    # def __init__(self, nums: List[int]):
    #     n = len(nums)
    #     self.dp = [[0] * (n+1) for _ in range(n+1)]
    #     for i in range(1, n+1):
    #         for j in range(i, n+1):
    #             self.dp[i][j] = self.dp[i][j-1] + nums[j-1]

    # def sumRange(self, left: int, right: int) -> int:
    #     return self.dp[left+1][right+1]
    
    '''
    把减法留在输出的时候
    考虑一条 nums 的所有输出需求也没有构建二维数组得多
    '''
    def __init__(self, nums: List[int]):
        self.sums = [0]
        for n in nums:
            self.sums.append(self.sums[-1] + n)
 
    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right+1] - self.sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

