#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        先排序
        然后指着最左边两个，在剩下的里面找最后一个
        每一轮跳过重复的
        '''
        result = []
        nums.sort() # O(logn)
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            k = len(nums)-1
            for j in range(i+1, len(nums)-1):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                # 这里开始其实可以改成二分搜索第三个数
                # 搜到了就是答案，搜不到就算了
                while j < k and nums[i] + nums[j] > -nums[k]:
                    k -= 1
                if j == k:
                    break
                
                if nums[i] + nums[j] == -nums[k]:
                    result.append([nums[i], nums[j], nums[k]])
        return result
            
# @lc code=end

