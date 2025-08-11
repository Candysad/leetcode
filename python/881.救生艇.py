#
# @lc app=leetcode.cn id=881 lang=python3
#
# [881] 救生艇
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        result = 0
        people.sort()
        left, right = 0, len(people) - 1
        while left < right:
            if people[right] + people[left] > limit:
                result += 1
                right -= 1
            else:
                result += 1
                left += 1
                right -= 1
        if left == right: result += 1
        return result  
# @lc code=end