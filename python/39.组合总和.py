#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
from heapq import *
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        是完全背包问题，但是要给出所有组合的情况
        同一个数可以多次选取
        '''
        n = len(candidates)
        candidates.sort()
        result = []
        
        '''
        用全局变量数组，单独回溯
        '''
        
        pre = []
        def dfs(i:int, pre_sum):
            if pre_sum == target:
                result.append(pre.copy())
                return
            
            if i == n or pre_sum > target:
                return

            # 不带当前数，向后
            dfs(i+1, pre_sum)
            
            # 带当前数，递归
            # 重复带当前数，或向后走（递归下一层实现）
            pre.append(candidates[i])
            dfs(i, pre_sum + candidates[i])
            pre.pop() # 回溯，把当前数弹出去
        
        dfs(0, 0)
        return result
        
        '''
        参数里传了数组，内存花销太大了
        '''
        # def dfs(i:int, pre:list, pre_sum:int):
            
        #     # print(i, pre, pre_sum)
        #     if (i == n and pre_sum != target) or pre_sum > target:
        #         return
            
        #     if pre_sum == target:
        #         result.append(pre)
        #         return
            
            
        #     # 不带当前数，向后
        #     dfs(i+1, pre.copy(), pre_sum)
            
        #     t = pre.copy()
        #     # 重复加上当前数
        #     if pre_sum + candidates[i] <= target:
        #         t = t.copy()
        #         t.append(candidates[i])
        #         pre_sum += candidates[i]
        #         dfs(i, t, pre_sum)
            
        # dfs(0, [], 0)    
        # return result  
# @lc code=end

