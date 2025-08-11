#
# @lc app=leetcode.cn id=422 lang=python3
#
# [422] 有效的单词方块
#

# @lc code=start
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        m = len(words)
        for i in range(m):
            t = []
            for j in range(m):
                if i >= len(words[j]): t.append(' ')
                else: t.append(words[j][i])
            
            t = ''.join(t).rstrip()
            if t != words[i]: return False
        
        return True
# @lc code=end