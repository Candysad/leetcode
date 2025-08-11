#
# @lc app=leetcode.cn id=2301 lang=python3
#
# [2301] 替换字符后匹配
#
from collections import defaultdict
# @lc code=start
class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        table = defaultdict(set)
        for k, v in mappings:
            table[k].add(v)
        n = len(s)
        sn = len(sub)
        
        targets = set()
        for j in range(sn, n + 1):
            targets.add(s[j-sn : j])
        if sub in targets: return True
        
        for target in targets:
            sign = True
            for i in range(sn):
                if sub[i] != target[i]:
                    if target[i] not in table[sub[i]]:
                        sign = False
                        break
            if sign: return True
        
        return False
                
                
# @lc code=end