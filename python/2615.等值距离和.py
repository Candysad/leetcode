#
# @lc app=leetcode.cn id=2615 lang=python3
#
# [2615] 等值距离和
#
from collections import defaultdict
# @lc code=start
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        table = defaultdict(list)
        for i, num in enumerate(nums):
            pre = table[num][-1][1] if table[num] else 0
            table[num].append([i, pre + i])
        
        for num in table:
            total = table[num][-1][1]
            n = len(table[num])
            for i in range(n):
                index, pre = table[num][i]
                nums[index] = total - pre - (n-1 - i) * index + (i+1) * index - pre
        return nums
# @lc code=end