#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        result = []
        path = []
        n = len(digits)
        def dfs(i):
            if i == n:
                result.append(''.join(path))
                return

            for c in phoneMap[digits[i]]:
                path.append(c)
                dfs(i+1)
                path.pop()
        
        dfs(0)
        return result    
# @lc code=end

