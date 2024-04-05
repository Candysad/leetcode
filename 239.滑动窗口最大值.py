#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
from collections import Counter, deque
from heapq import *
# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        双端单调队列
        对于长度k的窗口，只存k长度里最大的几个
        每次有新的进来，就把比新的小的全弄出去
        因为它们比新来的更早，本来也更早出去，而且它们小，直到退休都不会被现在这个大了，也就不会被记录进答案
        其实和优先队列记下标是一样的
        '''
        n = len(nums)
        queue = deque()
        for i, num in enumerate(nums[:k]):
            while queue and nums[queue[-1]] <= num:
                queue.pop()
            queue.append(i)
        result = [nums[queue[0]]]
        
        for i in range(k, n):
            num = nums[i]
            while queue and nums[queue[-1]] <= num:
                queue.pop()
            queue.append(i)
            
            if i - queue[0] >= k:
                queue.popleft()
            
            result.append(nums[queue[0]])
        return result

        '''
        Counter+优先队列懒更新
        不用counter就要记录堆里每个数的下标 (num, index)，比left还左的就不能要
        求最大值所以优先队列取反
        '''
        # n = len(nums)
        # counter = Counter(nums[:k])
        # left, right = 0, k
        # queue = [-num for num in nums[:k]]
        # heapify(queue)
        # result = [-queue[0]]
        
        # while right < n:
        #     counter[nums[left]] -= 1
        #     counter[nums[right]] += 1
        #     heappush(queue, -nums[right])
            
        #     while counter[-queue[0]] == 0:
        #         heappop(queue)
            
        #     result.append(-queue[0])
        #     left +=1
        #     right += 1
            
        # return result      
# @lc code=end

