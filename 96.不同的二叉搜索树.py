#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
dp = [1,1] # 0个和1个的情况都是1
for i in range(2, 20):
    dp.append(0)
    for j in range(0, i): # 左边最少0个，最多i-1个
        dp[-1] += dp[j] * dp[i-1 - j]

class Solution:
    def numTrees(self, n: int) -> int:
        '''
        推了一下把递推公式找出来了
        从根节点往下，左右两边的个数不同决定了整棵树的不同
        所以只需要枚举左右两边的个数情况，最后相加
        
        另一种用递推公式
        c_{n+1} = c_n * \frac{2(2n+1)}{n+2}
        '''
        return dp[n]

# @lc code=end

