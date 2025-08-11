#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
def hashlist(x: List):
    return ','.join([str(i) for i in x])

def dehashlist(x:str):
    return [int(i) for i in x.split(',')]

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        46.用了字典的技巧
        这里有重复数字就用不了了，改成Counter之类的数个数还行，但是内存会多用一倍Counter的部分
        或者把字典里的数字改成下标，最后再把下标改成对应的数字，但是这样没有去重
        再给每个排列出的序列算个hash，实现在result里去重的效果
        '''
        n = len(nums)
        result = set()
        def dfs(index=0):
            if index == n:
                result.add(hashlist(nums.copy()))
                return
            
            for i in range(index, n):
                nums[index], nums[i] = nums[i], nums[index]
                
                dfs(index+1)
                
                nums[index], nums[i] = nums[i], nums[index]
            
        dfs()
        return [dehashlist(x) for x in result]
# @lc code=end

