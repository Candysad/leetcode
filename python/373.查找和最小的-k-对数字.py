#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的 K 对数字
#
from heapq import *
# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''
        对于同一个索引i上的的两个数字(i, i)，其后面的所有组合都比他们大
        但是
            除了(i+x, i+y)的组合，也有 (i-x, i+y) 这样一边向前，一边向后的组合
            这种组合（ 相比 (i,i) ）可能变大也可能变小（变小是最致命的，因为会向前面的结果插入新的答案）
        解决办法是以其中一个队列的所有情况为基础，配合优先队列得到一定是前k大的组合
        '''
        
        result = []
        m, n = len(nums1), len(nums2)
        queue = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        heapify(queue)
        
        while queue and len(result) < k:
            _, i, j = heappop(queue)
            result.append([nums1[i], nums2[j]])
            
            if j < n-1:
                heappush(queue,(nums1[i]+nums2[j+1], i, j+1))
        

        return result
        
# @lc code=end

