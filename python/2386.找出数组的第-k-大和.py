#
# @lc app=leetcode.cn id=2386 lang=python3
#
# [2386] 找出数组的第 K 大和
#

# @lc code=start
class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        '''
        数学题
        在有正有负的序列里找不下标的数组合中第K大的和
        最大的和一定是所有正数的和
        然后剔除正数或加上负数变小
        那就是减去正数或负数的绝对值
        但是每次不一定减一个，而是减去一个序列（数字个数不定）的和

        先找正数之和
        再按从小到大排序所有数的绝对值

        再反过来想，已经得到最大的序列
        第一大的序列就是最大减去第一小的绝对值序列空序列
        第二大的序列就是最大减去第二小的绝对值序列
        第三大的序列就是最大减去第三小的绝对值序列
        第K 大的序列就是最大减去第k 小的绝对值序列
        
        找第 k 小的序列，小顶堆优先队列：
            所有数字构成的超集已排序,
            对于超集的不定元素个数的子序列，要对他们的序列和排序
            用小顶堆存储每个序列的和
            1.每个元素有取和不取两种情况,但是用递归太慢
            2.每次取出队列中上一次的和与序列中当前的数
                加入一种序列和：考虑将上一次取的数删去，也可看作用当前数替换上一个数
                加入另一种序列和：不做改变，单纯增加一个数
                上一次的和一定是第i大，当前数应大于等于上一次的数，故新加入的两种情况总有第i+1大的和
            3.删除上一个数和纯增加一个数都可以更新一种序列情况
            4.小顶堆会按从小到大保存序列和，每次取出第i小的
        '''
        n = len(nums)
        result = 0
        for i in range(n):
            if nums[i] > 0:
                result += nums[i]
            else:
                nums[i] = -nums[i]
        nums.sort()
        
        # 优先队列 (序列和， 当前数)
        k_min = 0
        pq = [(nums[0], 0)]     # 加入第2小的绝对值序列，预期找第k小的
        for _ in range(2, k + 1): # 优先队列从第2小开始拿，拿到第k个
            t, index = heappop(pq)
            if index != n - 1:
                heappush(pq, (t + nums[index+1], index+1))
                heappush(pq, (t - nums[index] + nums[index+1], index+1))
            k_min = t
        
        return result - k_min 
# @lc code=end

