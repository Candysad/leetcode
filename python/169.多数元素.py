#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
from collections import Counter
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Boyer-Moore
        一个有唯一个数超过总数一半的数组
        删去任意两个元素，原来的多数元素仍是新数组的多数元素
        
        删掉的不是多数元素，则多数仍然多数
        每次都删掉一个多数，则总量上多数比其他数字个数还多1个，总会剩余1个
        '''
        t = 0
        n = None
        for num in nums:
            if t == 0:
                n = num
                t += 1
            else:
                if n == num:
                    t += 1
                else:
                    t -= 1
        return n
        
        return Counter(nums).most_common()[0][0]
# @lc code=end

