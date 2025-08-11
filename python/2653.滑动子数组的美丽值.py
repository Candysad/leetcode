#
# @lc app=leetcode.cn id=2653 lang=python3
#
# [2653] 滑动子数组的美丽值
#
from collections import defaultdict
from heapq import *
# @lc code=start
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        '''
        优先队列
        大顶堆维护小的x个，堆顶即为答案
        小顶堆维护大的k-x个
        
        新来一个数，看放在哪一侧
        出一个数只能懒更新，看在哪一侧，如果在左侧，说明左侧缺了一个，从右侧补过来一个
        懒更新，两个堆只要在取堆顶的数就要先弹出过时信息
        '''
        n = len(nums)
        heapleft = [] # 大顶堆
        heapright = [] # 小顶堆
        
        left, right = 0, 0
        # 先全部放入右侧小顶堆
        while right < k:
            heappush(heapright, (nums[right], right))
            right += 1
        
        # 再把x个最小的放入左侧大顶堆
        for i in range(x):
            t = heappop(heapright)
            heappush(heapleft, (-t[0], t[1]))
        
        # 第一个答案
        t = -heapleft[0][0]
        result = [t if t < 0 else 0]
        while right < n:
            # 加入窗口右侧新的数
            num = nums[right]
            # 够小，放左边
            if num < -heapleft[0][0]:
                heappush(heapleft, (-num, right))
                # 此时左边多一个，匀给右边一个
                # 要取左侧最大值，先更新
                while heapleft[0][1] < left: # 懒更新弹出过时信息
                    heappop(heapleft)
                t = heappop(heapleft)
                heappush(heapright, (-t[0], t[1]))
            # 太大，放右边
            else:# 只用放，不需要懒更新
                heappush(heapright, (num, right))
            right += 1
            
            # 弹出滑到窗口外的数
            num = nums[left]
            # 在左侧堆里，弹出后左侧亏一个
            # 比堆顶小就肯定在左侧，和堆顶相等则下标更小则也在左侧
            # 此时左侧堆要么匀了一个给右侧，堆顶已经懒更新一次
            # 要么没动过，由上一轮的结尾懒更新
            if num < -heapleft[0][0] or (num == -heapleft[0][0] and heapleft[0][1] <= left):
                # 从右侧要一个过来
                while heapright[0][1] < left: # 懒更新弹出过时信息
                    heappop(heapright)
                t = heappop(heapright)
                heappush(heapleft, (-t[0], t[1]))
            # 在右侧堆里，那就无所谓了
            left += 1
            
            # 取左侧堆顶做当前窗口答案值
            while heapleft[0][1] < left:
                heappop(heapleft)
            t = -heapleft[0][0]
            result.append(t if t < 0 else 0)
        
        return result
        

        '''
        暴力滑窗
        '''
        # n = len(nums)
        # window = defaultdict(int)
        # for num in nums[:k]:
        #     window[num] += 1
        
        # result = []
        # for i in range(n-k+1):
        #     count = 0
        #     for t in range(-50, 0):
        #         count += window[t]
        #         if count >= x:
        #             result.append(t)
        #             break
            
        #     if count < x:
        #         result.append(0)
        
        #     if i+k < n:
        #         window[nums[i]] -= 1
        #         window[nums[i+k]] += 1
        
        # return result
# @lc code=end