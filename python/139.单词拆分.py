#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start

# dict 实现字典树
# def add(trie, word):
#     last = trie
#     for c in word:
#         # 存在就返回一个字典
#         # 不存在就返回一个空的字典
#         # 最后更新了都要再放进去
#         now = last.get(c, {"#end":False}) # 记录停止位置
#         last[c] = now
#         last = now
#     last["#end"] = True

# def find(trie, word):
#     last = trie
#     for c in word:
#         now = last.get(c, False)
#         if not now:
#             return False
#         last = now
#     return last["#end"]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        深度优先多半会超时
        爆内存了😓
        广度优先，感觉也会超时
        '''
        # queue = [s]
        # while queue:
        #     t = queue
        #     queue = []
        #     # print("queue: ", t)
        #     for subs in t:
        #         # print("s: ", subs)
        #         for word in wordDict:
        #             # print("word: ", word)
        #             if subs == word:
        #                 return True
        #             if subs.startswith(word):
        #             # if len(subs) >= len(word) and subs[:len(word)] == word:
        #                 queue.append(subs[len(word):])
        # return False 
        
        '''
        动态规划
        从前往后构建
        每次新加入一个字符导致后缀改变，之前的后缀记录不再起效
        但是之前的前缀有用，可以保留，只考虑新加入一个字符的后缀能不能匹配
        新加入一个字符后一旦匹配，则可以结束剩余枚举
        
        需要查新加入字符后的后缀是否出现在字典中
        可以用字典树
        python dict 实现字典树
        字典树怎么也这么慢啊😓
        '''
        # lengh = len(s)
        # trie = {}
        # min_lengh = len(wordDict[0])
        # for word in wordDict:
        #     add(trie, word)
        #     min_lengh = min(min_lengh, len(word))
        
        # dp = [True] + [False for i in range(len(s))]
        # for i in range(1, lengh+1):
        #     for j in range(i):
        #         if i-j < min_lengh:
        #             break
        #         if dp[j] and find(trie, s[j:i]):
        #             dp[i] = True
        #             break
        # return dp[-1]
    
        '''
        别人不用字典树直接枚举候选词怎么更快啊
        '''
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for j in range(len(s) + 1):
            for i in range(len(wordDict)):
                if j >= len(wordDict[i]):
                    dp[j] = dp[j] or (dp[j - len(wordDict[i])] and s[j - len(wordDict[i]) : j] == wordDict[i])
        return dp[len(s)]
# @lc code=end

