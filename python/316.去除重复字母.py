#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#
from collections import Counter
# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''
        栈
        右边还有且比当前字符更大的可以先丢掉
        每次保留字符更小的，使字典序更小
        重复的不用添加
        每次一定会添加当前字符，等下一次看有没有机会丢掉来更新
        '''
        if len(s) == 1:
            return s
        
        stack = []
        counter = Counter(s)
        pre = set()
        
        for c in s:
            counter[c] -= 1
            if c in pre:
                continue      
            
            while stack and c < stack[-1] and counter[stack[-1]]:
                pre.remove(stack.pop())
                
            stack.append(c)
            pre.add(c)
            
        return ''.join(stack)  
# @lc code=end

