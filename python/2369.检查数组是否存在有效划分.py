#
# @lc app=leetcode.cn id=2369 lang=python3
#
# [2369] 检查数组是否存在有效划分
#

# @lc code=start
def check2(num1, num2):
    return num1 == num2

def check3(num1, num2, num3):
    return (num1 == num2 == num3) or (num1 +2 == num2 + 1 == num3)

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        '''
        DP
        从前往后构建状态，每次向前找2或3个
        '''
        f = [False for _ in range(len(nums)+1)]
        f[0] = True # 增加开头一个边界
        # 状态是当前位置之前是否符合，不包含当前位置
        # 每次检查当前位置之前的 2 或 3 个，以及他们之前的状态
        # 最后一个位置是否符合要看第 n+1 个位置
        
        for i in range(2, len(nums)+1):
            f[i] = f[i-2] and check2(nums[i-2], nums[i-1])
            
            if i >= 3:
                f[i] = f[i] or (f[i-3] and check3(nums[i-3], nums[i-2], nums[i-1]))
        
        return f[-1]
# @lc code=end

