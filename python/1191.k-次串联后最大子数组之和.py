#
# @lc app=leetcode.cn id=1191 lang=python3
#
# [1191] K 次串联后最大子数组之和
#

# @lc code=start
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        
        t = min(2, k) * arr
        pre = t[0]
        result = t[0]
        for num in t[1:]:
            if pre >= 0:
                pre += num
            else:
                pre = num
            result = max(result, pre)
        
        if k >= 2:
            msum = 0
            bsum = 0
            for num in arr[::-1]:
                bsum += num
                msum  = max(bsum, msum)
                
            fmsum = 0
            fsum = 0
            for num in arr:
                fsum += num
                fmsum  = max(fmsum, fsum) 
            if bsum > 0:
                return max(result, (msum + (k-2) * bsum) + fmsum) % mod
            else:
                return max(result, 0) % mod
        else:
            return result % mod if result > 0 else 0
# @lc code=end