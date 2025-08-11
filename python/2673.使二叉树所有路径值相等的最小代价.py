#
# @lc app=leetcode.cn id=2673 lang=python3
#
# [2673] 使二叉树所有路径值相等的最小代价
#

# @lc code=start
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        '''
        按最高的路径为标准调整剩下的
        调整父节点效率更高
        但是分支值更大的先达到标准后，小的需要单独调整
        
        反过来从下往上想，先每次平衡分岔两边，再往上调整父一级的两个兄弟节点
        因为下面分岔先调整一致，可以将下方的值加到父级来表示从此节点往下的整体
        '''
        left, right = n - 2, n - 1
        result = 0
        while left > 0:
            result += abs(cost[left] - cost[right])
            # cost[right // 2 - 1] += max(cost[left], cost[right])
            cost[left // 2] += max(cost[left], cost[right])
            
            left -= 2
            right -= 2
            
        return result       
# @lc code=end

