#
# @lc app=leetcode.cn id=2121 lang=python3
#
# [2121] 相同元素的间隔之和
#
from collections import defaultdict
# @lc code=start
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        table = defaultdict(list)
        for i, c in enumerate(arr):
            if table[c]:
                table[c].append(table[c][-1] + i) # 记录前缀和
            else:
                table[c].append(i)
        
        for key in table:
            tlist = table[key]
            n = len(tlist)
            # 最小下标
            arr[tlist[0]] = tlist[-1] - n*tlist[0]
            if n > 1:
                # 最大下标
                index = tlist[-1] - tlist[-2]
                arr[index] = n*index - tlist[-1]
                
                # 中间的
                for i in range(1, n-1):
                    index = tlist[i] - tlist[i-1]
                    # 比它小的被它减
                    # 比它大的减它
                    arr[index] = i * index - tlist[i-1] + (tlist[-1] - tlist[i]) - (n-1-i) * index
        return arr
# @lc code=end

