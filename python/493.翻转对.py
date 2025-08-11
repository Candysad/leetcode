#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        '''
        归并排序
        后面那组如果更小就计数 1*前面剩下的长度
        '''
        def merge(start1, start2, end2):
            result = 0
            t = []
            p1, p2 = start1, start2
            
            # 计数条件和合并条件分开...
            while p1 < start2 and p2 <= end2:
                if nums[p1] > 2*nums[p2]:
                    result += start2 - p1
                    p2 += 1
                else:
                    p1 += 1

            p1, p2 = start1, start2
            while p1 < start2 and p2 <= end2:
                if nums[p1] <= nums[p2]:
                    t.append(nums[p1])
                    p1 += 1
                else:
                    t.append(nums[p2])
                    p2 += 1
            t.extend(nums[p1:start2])
            t.extend(nums[p2:end2+1])        
                    
            nums[start1: end2+1] = t
            return result
        
        def merge_sort(left, right):
            if left >= right: return 0
            
            result = 0
            mid = left + ((right - left) >> 1)
            result += merge_sort(left, mid)
            result += merge_sort(mid+1, right)
            result += merge(left, mid+1, right)
            return result
        
        return merge_sort(0, len(nums)-1)

        '''
        树状数组
        '''
        # vis = set()
        # for num in nums:
        #     vis.add(num)
        #     vis.add(num // 2 if num % 2 else num // 2 - 1)
        
        # vis = sorted(list(vis))
        # table = {num : i+1 for i, num in enumerate(vis)}
        
        # n = len(vis)
        # fens = [0] * (n+1)
        # def lowerbit(i):
        #     return i & -i

        # def update(i, delta):
        #     while i <= n:
        #         fens[i] += delta
        #         i += lowerbit(i)
        
        # def get(i):
        #     result = 0
        #     while i:
        #         result += fens[i]
        #         i -= lowerbit(i)
        #     return result

        # result = 0
        # for num in nums[::-1]:
        #     i = table[num // 2 if num % 2 else num // 2 - 1]
        #     result += get(i)
        #     i = table[num]
        #     update(i, 1)
        # return result
# @lc code=end

