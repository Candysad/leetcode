#
# @lc app=leetcode.cn id=1562 lang=python3
#
# [1562] 查找大小为 M 的最新分组
#

# @lc code=start
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        table = [0] * (len(arr) + 2) # 最两头空出来
        result = -1
        for i, num in enumerate(arr):
            leftl, rightl = table[num-1], table[num+1]
            now = leftl + rightl + 1
            
            table[num - leftl] = now
            table[num + rightl] = now
            
            if now == m: result = i + 1
        
        return result    
# @lc code=end