#
# @lc app=leetcode.cn id=1793 lang=python3
#
# [1793] 好子数组的最大分数
#

# @lc code=start
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        '''
        左右指针
        条件是分别移动指针可以通过题干条件限定得到更好的答案
        本质上是条件满足了贪心并利用了限定位置 k 两侧这一结构条件而使用左右指针
        '''
        n = len(nums)
        left, right, pivot = k-1, k+1, nums[k]
        result = 0
        while pivot != -1:  
            while left >= 0 and nums[left] >= pivot:
                left -= 1
            while right < n and nums[right] >= pivot:
                right += 1
            result = max(result, (right- left - 1) * pivot)
            # 每次都使pivot为左右更大的那个
            # 进而下一次这一侧一定会出现更小的或达到边界终止
            # 所以整体是每次都可能得到更好的答案
            pivot = max((-1 if left == -1 else nums[left]), (-1 if right == n else nums[right]))
        
        return result
            
# @lc code=end

