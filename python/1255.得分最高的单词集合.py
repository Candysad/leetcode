#
# @lc app=leetcode.cn id=1255 lang=python3
#
# [1255] 得分最高的单词集合
#
from collections import defaultdict
from collections import Counter
# @lc code=start
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        alls = Counter(letters)
        wc = []
        for word in words:
            wc.append(Counter(word))
        
        def toscore(table):
            result = 0
            for c in table:
                result += table[c] * score[ord(c) - ord('a')]
            return result
        
        result = 0
        now = Counter()
        n = len(wc)
        def dfs(i):
            nonlocal now, result
            if now <= alls:
                result = max(result, toscore(now))
            else:
                return
            if i == n: return
            
            now += wc[i]
            dfs(i+1)
            now -= wc[i]
            
            dfs(i+1)

        dfs(0)
        return result
# @lc code=end