#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pre = {n:-1 for n in nums1}
        stack = []
        
        for n in nums2:
            while stack and stack[-1] < n:
                last = stack.pop()
                if pre.get(last, -1) == -1:
                    pre[last] = n
            
            stack.append(n)
        for i, n in enumerate(nums1):
            nums1[i] = pre[n]
        return nums1

# @lc code=end