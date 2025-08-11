#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path + '/'
        t = []
        for c in path:
            if not t:
                t.append(c)
            elif t[-1] == '/' and c == '/':
                continue
            else:
                t.append(c)
        
        t = ''.join(t)[1:-1].split('/')
        stack = ['/']
        for p in t:
            if p == '.': continue
            elif p == '..':
                if stack[-1] == '/': continue
                else: stack.pop()
            else:
                stack.append(p)
        
        return '/' + '/'.join(stack[1:])    
# @lc code=end