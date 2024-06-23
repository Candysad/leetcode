#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper(): return True
        if word == word.lower(): return True
        if len(word) > 1 and word == word[0].upper() + word[1:].lower(): return True
        return False    
# @lc code=end