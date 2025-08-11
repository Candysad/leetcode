#
# @lc app=leetcode.cn id=2951 lang=python3
#
# [2951] 找出峰值
#

# @lc code=start
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        lastt = 0 # 0 之前相等 # 1 之前更大 # -1 之前更小
        result = []
        for i in range(1, len(mountain)):
            if mountain[i-1] > mountain[i]:
                if lastt == 1:
                    result.append(i-1)
                lastt = -1
            elif mountain[i-1] == mountain[i]:
                lastt = 0
            else:
                lastt = 1
        return result
# @lc code=end

