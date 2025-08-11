#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        # 表，一次遍历实现找+建表
        
        for i in range(len(nums)):
            # 找另一半
            if dic.get(target - nums[i], "no") != "no":
                return [i, dic[target - nums[i]]]
            
            # 加入表
            dic[nums[i]] = i
            
            
# @lc code=end

