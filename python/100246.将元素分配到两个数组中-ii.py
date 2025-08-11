#
# @lc app=leetcode.cn id=100246 lang=python3
#
# [100246] 将元素分配到两个数组中 II
#
from bisect import bisect_left, bisect_right
# @lc code=start
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        '''
        二分
        '''
        stack1 = [nums[0]]
        stack2 = [nums[1]]
        n1, n2 = 1, 1
        
        for num in nums[2:]:
            i1 = bisect_right(stack1, num)
            i2 = bisect_right(stack2, num)
            
            gc1 = n1 - i1
            gc2 = n2 - i2
            
            if gc1 > gc2:
                stack1.insert(bisect_left(stack1, num), num)
                n1 += 1
            elif gc1 < gc2:
                stack2.insert(bisect_left(stack2, num), num)
                n2 += 1
            else:
                if n2 < n1:
                    stack2.insert(bisect_left(stack2, num), num)
                    n2 += 1
                else:
                    stack1.insert(bisect_left(stack1, num), num)
                    n1 += 1
        return stack1 + stack2
        
        
        '''
        树状数组
        '''
        # def lowerbit(i):
        #     return i & (-i)

        # def update(tree, i):
        #     while i < len(tree):
        #         tree[i] += 1
        #         i += lowerbit(i)
        
        # def get(tree, i):
        #     result = 0
        #     while i:
        #         result += tree[i]
        #         i -= lowerbit(i)
        #     return result
        
        # counter = set(nums)
        # table = {num:i+1 for i, num in enumerate(sorted(list(counter)))}
        # n = len(table)
        
        # stack1, stack2 = [], []
        # tree1 = [0] * (n + 1)
        # tree2 = [0] * (n + 1)
        # n1, n2 = 1, 1
        # stack1.append(nums[0])
        # update(tree1, table[nums[0]])
        # stack2.append(nums[1])
        # update(tree2, table[nums[1]])
        
        # for num in nums[2:]:
        #     i = table[num]
        #     gc1 = n1 - get(tree1, i)
        #     gc2 = n2 - get(tree2, i)
            
        #    if gc1 > gc2:
        #        stack1.append(num)
        #        n1 += 1
        #        update(tree1, i)
        #    elif gc1 < gc2:
        #        stack2.append(num)
        #        n2 += 1
        #        update(tree2, i)
        #    else:
        #        if n2 < n1:
        #            stack2.append(num)
        #            n2 += 1
        #            update(tree2, i)
        #        else:
        #            stack1.append(num)
        #            n1 += 1
        #            update(tree1, i)
        
        # return stack1 + stack2
# @lc code=end