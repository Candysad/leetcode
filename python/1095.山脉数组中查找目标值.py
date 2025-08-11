#
# @lc app=leetcode.cn id=1095 lang=python3
#
# [1095] 山脉数组中查找目标值
#
from bisect import bisect_left
# @lc code=start
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        
        @cache
        def find(i):
            return mountain_arr.get(i)
        
        def bisetleft(leftstart):
            i = bisect_left(list(range(leftstart)), target, key=lambda i: find(i))
            if find(i) == target:
                return i
            else:
                return -1
            
        def bisetright(rightstart):
            t = list(range(n-1, rightstart-1, -1))
            i = bisect_left(t, target, key=lambda i: find(i))

            if i == len(t): return -1
            if find(t[i]) == target:
                return t[i]
            else: 
                return -1
            return -1
            
        leftstart, rightstart = None, None # 左右两侧之后二分的起点
        preright = None # 右侧提前找到
        
        left, right = 0, n-1
        while leftstart is None or rightstart is None:
            if left >= right: # 单独判断极限停止位置
                leftn, rightn = find(left), find(right)
                if leftn == target: return left
                elif rightn == target: return right
                elif leftn < target and rightn < target:
                    return -1
                else:
                    if leftstart is None:
                        if leftn > target:
                            leftstart = left
                        if rightn > target:
                            leftstart = right
                    if rightstart is None:
                        if rightn > target:
                            rightstart = right
                        if leftn > target:
                            rightstart = left
                    break
            # 二分
            mid = left + ((right - left) >> 1)
            midn, midrn = find(mid), find(mid+1)
            if midrn > midn: # 左侧递增
                # 直接就找到了
                if midn == target: return mid
                if midrn == target: return mid+1

                if leftstart is None:
                    if midrn > target:
                        if midn < target: # 左侧没有目标
                            leftstart = 0
                        else:
                            leftstart = mid+1

                    if midn > target: leftstart = mid
                
                left = mid+1
                
            else: # 右侧递减
                # 这边找到了也不能立即返回，因为可能还在另一边
                if preright is None:
                    if midn == target:
                        preright = mid
                        rightstart = mid
                    if midrn == target:
                        preright = mid+1
                        rightstart = mid

                if rightstart is None:
                    if midn > target:
                        if midrn < target:
                            rightstart = n-1
                        else:
                            rightstart = mid
                    if midrn > target:
                        rightstart = mid+1
                
                right = mid

        result = bisetleft(leftstart)
        if result != -1:
            return result
        
        if preright is not None:
            return preright
        
        result = bisetright(rightstart)
        return result 
# @lc code=end