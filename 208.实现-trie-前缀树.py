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
        node = self.tree
        for i, c in enumerate(word):
            next_node = node.get(c, -1)
            if next_node == -1:
                node[c] = {}
                node = node[c]
            else:
                node = next_node
            
            if i == len(word)-1:
                node['end'] = 1

    def search(self, word: str) -> bool:
        node = self.tree
        for c in word:
            next_node = node.get(c, -1)
            if next_node == -1:
                return False
            else:
                node = next_node
            
        return True if node.get('end',0) else False
            
    def startsWith(self, prefix: str) -> bool:
        node = self.tree
        for c in prefix:
            next_node = node.get(c, -1)
            if next_node == -1:
                return False
            else:
                node = next_node
        return True
            
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

