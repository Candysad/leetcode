#
# @lc app=leetcode.cn id=2924 lang=python3
#
# [2924] 找到冠军 II
#

# @lc code=start
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        '''
        把输过的踢了
        从来没输过的就是冠军
        所有edge都有用，必须全部遍历
        '''
        result = set([i for i in range(n)])
        for left, right in edges:
            if right in result:
                result.remove(right)
        
        if len(result) != 1:
            return -1
        
        return result.pop()
        
# @lc code=end

