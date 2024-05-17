#
# @lc app=leetcode.cn id=1541 lang=python3
#
# [1541] 平衡括号字符串的最少插入次数
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        '''
        栈
        '''
        stack = []
        result = 0
        for c in s:
            if c == '(':
                if stack and stack[-1] == ')':
                    result += 1
                    stack.pop()
                    stack.pop()
                stack.append('(')
            else:
                if stack:
                    if stack[-1] == ')':
                        stack.pop()
                        stack.pop()
                    else:
                        stack.append(')')
                else:
                    result += 1
                    stack.append('(')
                    stack.append(')')
        while stack:
            if stack[-1] == ')':
                result += 1
                stack.pop()
                stack.pop()
            else:
                result += 2
                stack.pop()
        return result
            
 
        '''
        右括号要两个连续
        但不需要贴在左括号上
        '''
        n = len(s)
        result = 0
        needright = 0 # 需要1组2个连续右括号
        
        i = 0
        while i < n:
            # 来一个左括号，需要一组新的右括号
            if s[i] == '(':
                needright += 1
            else:
                # 右括号且现在需要
                if needright:
                    # 后一个不是右括号或者没有后一个了
                    if (i < n-1 and s[i+1] != ')') or i == n-1:
                        result += 1 # 补一个
                    else:
                        # 后一个是的话跳过下一个
                        i += 1
                         
                    # 后一个是不是右括号这里都处理了一组需求
                    needright -= 1
                else:
                    # 不需要右括号你来一个
                    # 说明需要左括号
                    result += 1 # 补一个左括号
                    # 此时需要两个连续右括号，看一眼下一个
                    # 下一个不是右括号
                    if (i < n-1 and s[i+1] != ')') or i == n-1:
                        result += 1 # 补一个
                    else:
                        # 后一个是的话跳过下一个
                        i += 1
            i += 1
        return result + 2 * needright
    
    
    
            
# @lc code=end

