#
# @lc app=leetcode.cn id=321 lang=python3
#
# [321] 拼接最大数
#

# @lc code=start
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def stackformaxn(nums, x):
                n = len(nums)
                
                stack = []
                i = 0
                while i < n:
                    if len(stack) + n-i == x:
                        stack.extend(nums[i:])
                        return stack
                    
                    while stack and stack[-1] < nums[i] and len(stack)-1 + n-i >= x:
                        stack.pop()
                    
                    if len(stack) < x:
                        stack.append(nums[i])
                    i += 1
                
                return stack
            
        def search(nums1:list, nums2:list):
            p1 = 0
            n = len(nums1)
            p2 = 0
            m = len(nums2)
            result = []
            
            while p1 < n and p2 < m:
                if compare(nums1[p1:], nums2[p2:]):
                    result.append(nums1[p1])
                    p1 += 1
                else:
                    result.append(nums2[p2])
                    p2 += 1
            if p1 < n and p2 == m:
                result.extend(nums1[p1:])
            if p2 < m and p1 == n:
                result.extend(nums2[p2:])
            
            return result
        
        def compare(nums1:list, nums2:list):
            n = len(nums1)
            m = len(nums2)
            p = 0
            while p < n and p < m:
                if nums1[p] > nums2[p]:
                    return True
                elif nums1[p] < nums2[p]:
                    return False
                else:
                    p += 1
            
        
            if p == n and p < m:
                return False
            if p == m and p <= n:
                return True
        
        result = [0] * k
        for i in range(max(0, k-len(nums2)), min(k, len(nums1))+1):
            j = k - i
            n1 = stackformaxn(nums1, i)
            n2 = stackformaxn(nums2, j)
            t = search(n1, n2)
            if compare(result, t) == False:
                result = t
            
        return result
                
# @lc code=end

