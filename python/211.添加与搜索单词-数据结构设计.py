#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#

# @lc code=start
class WordDictionary:

    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        now = self.tree
        for c in word:
            next = now.get(c, {"end": False})
            now[c] = next
            now = next
        now["end"] = True

    def search(self, word: str) -> bool:
        n = len(word)
        def dfs(now, i):
            if i == n:
                if now['end']: return True
                return False
            
            c = word[i]
            t = False
            if c == '.':
                for key in now:
                    if key == 'end': continue
                    
                    t |= dfs(now[key], i+1)
            
            else:
                if c not in now: return False
                
                t = dfs(now[c], i+1)
            
            return t
        
        return dfs(self.tree, 0)
# @lc code=end