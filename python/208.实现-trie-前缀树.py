#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        now = self.tree
        for c in word:
            next = now.get(c, {"end": False})
            now[c] = next
            now = next
        now["end"] = True

    def search(self, word: str) -> bool:
        now = self.tree
        for c in word:
            next = now.get(c, None)
            if next is None: return False
            now = next
        return now["end"]
        

    def startsWith(self, prefix: str) -> bool:
        now = self.tree
        for c in prefix:
            next = now.get(c, None)
            if next is None: return False
            now = next
        return True
# @lc code=end

