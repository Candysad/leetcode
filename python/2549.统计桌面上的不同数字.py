#
# @lc app=leetcode.cn id=2549 lang=python3
#
# [2549] 统计桌面上的不同数字
#

# @lc code=start
class Solution:
    def distinctIntegers(self, n: int) -> int:
        '''
        数学题
        题目中 n 最大才100，但是会放10**9天
        每次放都有 x % i == 1
        即x-1整除i，则i最大为x-1
        即每天每个已经放上来的数x_k都会增加 x_{k+1} = x_k - 1
        可能会重复，但是不重要，因为 10**9太大了，最终1到n-1（最大才99）全都会放上来
        '''
        return 1 if n == 1 else n - 1 
        
# @lc code=end

