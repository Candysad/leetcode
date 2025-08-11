#
# @lc app=leetcode.cn id=1411 lang=python3
#
# [1411] 给 N x 3 网格图涂色的方案数
#
from functools import cache
# @lc code=start
class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        
        table = {
            "all": ['grg','gry','gyg','gyr','rgr','rgy','ryg','ryr','ygr','ygy','yrg','yry'],
            'yry': ['rgr', 'gyr', 'ryg', 'gyg', 'ryr'],
            'gry': ['rgr', 'ygr', 'ryg', 'ryr'],
            'rgr': ['yry', 'gry', 'grg', 'gyg', 'yrg'],
            'rgy': ['gyr', 'grg', 'gyg', 'yrg'],
            'gyr': ['yry', 'rgy', 'ygy', 'yrg'],
            'grg': ['rgr', 'rgy', 'ygr', 'ygy', 'ryr'],
            'ygr': ['gry', 'grg', 'ryg', 'gyg'],
            'ryg': ['yry', 'gry', 'ygr', 'ygy'],
            'ygy': ['gyr', 'grg', 'ryg', 'gyg', 'ryr'],
            'gyg': ['yry', 'rgr', 'rgy', 'ygr', 'ygy'],
            'ryr': ['yry', 'gry', 'grg', 'ygy', 'yrg'],
            'yrg': ['rgr', 'rgy', 'gyr', 'ryr']
        }
        
        @cache
        def dfs(i, state):
            if i == n: return 1
            
            t = 0
            for nextstate in table[state]:
                t += dfs(i+1, nextstate)
            return t % mod
        
        return dfs(0, "all")
# @lc code=end