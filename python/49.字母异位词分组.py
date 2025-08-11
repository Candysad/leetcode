#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
from collections import defaultdict
# @lc code=start

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        hash给每个组合存下来
        '''
        
        '''
        用字符串本身做key
        '''
        # word_hash = defaultdict(list)
        # for s in strs:
        #     s_hash = ''.join(sorted(s))
        #     word_hash[s_hash].append(s)
        
        # return list(word_hash.values())
    
    
        '''
        用字符出现次数做key
        '''
        def getHash(s:str):
            td = [0] * 26
            for c in s:
                td[ord(c) - ord('a')] += 1
            return str(td)
        
        word_hash = defaultdict(list)
        for s in strs:
            s_hash = getHash(s)
            word_hash[s_hash].append(s)
        
        return list(word_hash.values())
# @lc code=end

