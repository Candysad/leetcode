#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        
        # s = str(x)
        s = []
        while x:
            s.append(x % 10)
            x = x // 10
        
        left = 0
        right = len(s)-1
        while right > left and s[left] == s[right]:
            left += 1
            right -= 1
        
        if right <= left:
            return True
        
        return False
# @lc code=end

