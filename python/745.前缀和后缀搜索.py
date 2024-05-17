#
# @lc app=leetcode.cn id=745 lang=python3
#
# [745] 前缀和后缀搜索
#

# @lc code=start
'''
字典树
存 前缀（从前往后） # 后缀（从后往前） 
结束位置存出现的i
从前往后遍历word，使结束位置i最大
'''
# char_Length = 27 # 英文字母 + #分隔 
# first_char = 'a'
# class Trie:
#     def __init__(self) -> None:
#         self.tree = [[0 for i in range(char_Length)]]
#         self.count = 0
#         self.end = [-1]
    
#     def add(self, s:str, index:int):
#         now = 0
#         for c in s:
#             ic = 26 if c == '#' else ord(c) - ord(first_char)
#             if not self.tree[now][ic]:
#                 self.tree.append([0 for i in range(char_Length)])
#                 self.count += 1
#                 self.tree[now][ic] = self.count
#                 self.end.append(-1)
                
#             now = self.tree[now][ic]

#         self.end[now] = index
    
#     def find(self, s:str):
#         now = 0
#         for c in s:
#             ic = 26 if c == '#' else ord(c) - ord(first_char)
#             if not self.tree[now][ic]:
#                 return -1
#             now = self.tree[now][ic]
#         return self.end[now]

class WordFilter:
    '''
    暴力存入所有情况记录下的最大下标
    空间换时间
    '''
    def __init__(self, words: List[str]):
        self.dictT = {}
        for i, word in enumerate(words):
            word_length = len(word)
            for prelen in range(1, word_length + 1):# 做后面的下标
                                                    # 在 (0,n-1) 从 1 到 n 
                for sufflen in range(word_length):  # 做前面的下标
                                                    #从-1 到 -n
                    self.dictT[word[:prelen]+ "!" + word[-sufflen:]] = i

    def f(self, pref: str, suff: str) -> int:
        return self.dictT.get(pref + "!" + suff, -1)
    '''
    字典树
    用数组的好慢
    '''
    # def __init__(self, words: List[str]):
    #     self.trie = Trie()
    #     for i, word in enumerate(words):
    #         for j in range(1, len(word)+1):
    #             for k in range(len(word), 0, -1):
    #                 self.trie.add(word[:j] + "#" + word[-1:-1-k:-1], i)


    # def f(self, pref: str, suff: str) -> int:
    #     return self.trie.find(pref + "#" + suff[::-1])
    
    '''
    字典树
    用字典的
    也不快...
    '''
    # def __init__(self, words: List[str]):
    #     self.trie = {}
    #     self.weightKey = ('#', '#')
    #     for i, word in enumerate(words):
    #         cur = self.trie
    #         m = len(word)
    #         for j in range(m):
    #             tmp = cur
    #             for k in range(j, m):
    #                 key = (word[k], '#')
    #                 if key not in tmp:
    #                     tmp[key] = {}
    #                 tmp = tmp[key]
    #                 tmp[self.weightKey] = i
    #             tmp = cur
    #             for k in range(j, m):
    #                 key = ('#', word[-k - 1])
    #                 if key not in tmp:
    #                     tmp[key] = {}
    #                 tmp = tmp[key]
    #                 tmp[self.weightKey] = i
    #             key = (word[j], word[-j - 1])
    #             if key not in cur:
    #                 cur[key] = {}
    #             cur = cur[key]
    #             cur[self.weightKey] = i
                
    # def f(self, pref: str, suff: str) -> int:
    #     cur = self.trie
    #     for key in zip_longest(pref, suff[::-1], fillvalue='#'):
    #         if key not in cur: 
    #             return -1
    #         cur = cur[key]
    #     return cur[self.weightKey]
# @lc code=end

