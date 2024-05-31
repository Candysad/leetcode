#
# @lc app=leetcode.cn id=966 lang=python3
#
# [966] 元音拼写检查器
#

# @lc code=start
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        table = set(wordlist)
        tablecap = {}
        tablevow = {}
        
        for word in wordlist:
            tablecap.setdefault(word.lower(), word)
            vw = ''.join(["*" if c in 'aeiou' else c for c in word.lower()])
            tablevow.setdefault(vw, word)
        
        def check(word:str):
            if word in table:
                return word
            
            if word.lower() in tablecap:
                return tablecap[word.lower()]
            
            vw = ''.join(["*" if c in 'aeiou' else c for c in word.lower()])
            if vw in tablevow:
                return tablevow[vw]
            return ''
        
        return list(map(check, queries))
        
        
# @lc code=end

