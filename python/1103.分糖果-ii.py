#
# @lc app=leetcode.cn id=1103 lang=python3
#
# [1103] 分糖果 II
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        i = 0
        c = 1
        while candies > 0:
            delta = min(c, candies)
            result[i] += delta
            candies -= delta
            i = (i + 1) % num_people
            c += 1
            
        return result
        
# @lc code=end

