#
# @lc app=leetcode.cn id=948 lang=python3
#
# [948] 令牌放置
#

# @lc code=start
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        low, high = 0, len(tokens) - 1
        result = 0
        now = 0
        
        while low <= high:
            if power >= tokens[low]:
                power -= tokens[low]
                now += 1
                low += 1
                
                result = max(result, now)
            else:
                if now == 0:
                    break
                
                now -= 1
                power += tokens[high]
                high -= 1
        return result
# @lc code=end

