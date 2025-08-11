#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        深度优先
        递归
        时间和下面广度优先是一样的
        '''
        result = []
        n = len(nums)
        def dfs(index = 0):
            if index == n:
                result.append(nums.copy())
                return
            
            # index 是当前要换成其他数字的位置
            for i in range(index, n):
                nums[index], nums[i] = nums[i], nums[index]
                
                # 去换下一个位置
                dfs(index+1)
                
                # 换回来，这一层index和下一个位置i换
                nums[index], nums[i] = nums[i], nums[index]
        
        dfs()
        return result
        
        '''
        广度优先
        全排列
        '''
        nums = set(nums)
        n = len(nums)
        queue = [{}]
        
        result = []
        while queue:
            t = queue
            queue = []
            for pre in t:
                if len(pre) == n:
                    result.append(list(pre))
                    continue
                for num in nums:
                    t_pre = pre.copy()
                    if num not in t_pre:
                        t_pre[num] = None
                        queue.append(t_pre)
        return result

# @lc code=end