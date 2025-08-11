#
# @lc app=leetcode.cn id=2135 lang=python3
#
# [2135] 统计追加字母可以获得的单词数
#

# @lc code=start
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        table = set()
        def encode(word):
            code = 0
            for c in word:
                bit = ord(c) - ord('a')
                code |= 1 << bit
            return code
        
        for word in startWords:
            table.add(encode(word))
        
        
        def check(code):
            for i in range(26):
                if (code >> i) & 1:
                    if code ^ (1 << i) in table:
                        return True  
            return False
            
        result = 0
        for word in targetWords:
            if check(encode(word)): result += 1
        return result
# @lc code=end