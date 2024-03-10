#
# @lc app=leetcode.cn id=745 lang=python3
#
# [745] 前缀和后缀搜索
#

# @lc code=start
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
    '''
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
# @lc code=end

