#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        pre = []
        def dfs(i, res, pre_sum):
            if k and pre_sum>= n:
                return
            if k == 0:
                if pre_sum == n:
                    result.append(pre.copy())
                return
            
            if i == 9:
                return
            
            # 带当前数字
            pre.append(i)
            dfs(i+1, res-1, pre_sum+i)
            # 不带当前数字
            pre.pop()
            dfs(i+1, res, pre_sum)
        
        dfs(1, k)
        return result

# @lc code=end

