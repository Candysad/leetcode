#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        两遍单调栈确定每个基本矩形高度的左右最远可用范围
        一次遍历得到答案
        
        进一步
        起始一次遍历过去的时候，直接确定了右侧边界
        
        而入栈的时候就确认了左侧边界
        因为单调栈里入栈的元素一定大于等于里面剩下的
        也就是说入栈的时候栈里的元素都在入栈元素的左边，而且有比它小的
        '''
        n = len(heights)
        left = [0] * n # 左侧边界
        right = [n-1] * n # 右侧边界
        
        # 找每个高度的右侧最远可达位置
        stack = []
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                lasti = stack.pop()
                right[lasti] = i - 1
            if stack: # 入栈顺便确定左边界
                if heights[stack[-1]] < h:
                    left[i] = stack[-1]+1
                else: # heights[stack[-1]] == h
                    left[i] = left[stack[-1]]
            stack.append(i)
        
        # # 左侧
        # stack = []
        # for i, h in enumerate(heights[::-1]):
        #     i = n-1-i
        #     while stack and heights[stack[-1]] > h:
        #         lasti = stack.pop()
        #         left[lasti] = i + 1
        #     stack.append(i)
        # print(right)
        # print(left)
        return max([heights[i] * (right[i] - left[i] +1) for i in range(n)])
# @lc code=end

