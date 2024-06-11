#
# @lc app=leetcode.cn id=3012 lang=python3
#
# [3012] 通过操作使数组长度最小
#
from collections import Counter
# @lc code=start
class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        counter = Counter(nums)
        nums = sorted(counter.keys())
        _min = nums[0]
        right = 1
        n = len(nums)
        while _min != 1 and right < n:
            t1 = _min % nums[right]
            t2 = nums[right] % _min
            t1 = t1 if t1 else _min
            t2 = t2 if t2 else _min
            _min = min(_min, t1, t2)
            right += 1
        
        if _min < nums[0]:
            return 1
        return (counter[_min] + 1) // 2
# @lc code=end