#
# @lc app=leetcode.cn id=1298 lang=python3
#
# [1298] 你能从盒子里获得的最大糖果数
#

# @lc code=start
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        vis = set()
        candidate  = initialBoxes
        queue = []
        for box in candidate:
            if status[box]:
                vis.add(box)
                queue.append(box)
            
        result = 0
        while queue:
            t = queue
            queue = []
            
            for box in t:
                result += candies[box]
                for key in keys[box]:
                    status[key] = 1
                
                candidate.extend(containedBoxes[box])
                for nextbox in candidate:
                    if nextbox not in vis and status[nextbox]:
                        queue.append(nextbox)
                        vis.add(nextbox)
        
        return result 
# @lc code=end