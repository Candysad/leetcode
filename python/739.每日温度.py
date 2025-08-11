#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        stack [index...]
        单调栈
        每次来一个就把前面比它小的都出了
        然后放入这一个
        '''
        result = [0] * len(temperatures)
        stack  = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                    lasti = stack.pop()
                    result[lasti] = i - lasti
            stack.append(i)
        
        return result
# @lc code=end

