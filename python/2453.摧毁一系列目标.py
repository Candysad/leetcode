#
# @lc app=leetcode.cn id=2453 lang=python3
#
# [2453] 摧毁一系列目标
#

# @lc code=start
class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        nums.sort()
        counter = {}
        for n in nums:
            t = n % space
            if t in counter:
                counter[t][1] += 1
            else:
                counter[t] = [n, 1]
        
        resulti = -1
        resultc = 0
        for key in counter:
            if counter[key][1] > resultc:
                resulti = counter[key][0]
                resultc = counter[key][1]
        
        return resulti

# @lc code=end

