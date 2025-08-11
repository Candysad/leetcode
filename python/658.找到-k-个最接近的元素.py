#
# @lc app=leetcode.cn id=658 lang=python3
#
# [658] 找到 K 个最接近的元素
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        python 1行
        '''
        return sorted(sorted(arr, key=lambda t: abs(t-x))[:k])
# @lc code=end

