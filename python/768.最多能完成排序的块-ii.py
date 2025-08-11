#
# @lc app=leetcode.cn id=768 lang=python3
#
# [768] 最多能完成排序的块 II
#

# @lc code=start
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        counter = Counter(arr)
        table = defaultdict(int)
        tsum = 0
        for num in sorted(list(counter.keys())):
            tsum += counter[num]
            table[num] = tsum

        spans = []
        for i, num in enumerate(arr[::-1]):
            i = tsum - i - 1
            table[num] -= 1
            j = table[num]
            spans.append([i, j] if i < j else [j, i])
        spans.sort()

        pre = 0
        limit = spans[0][1]
        result = []
        for left, right in spans[1:]:
            if limit > left:
                limit = max(limit, right)
            else:
                result.append([pre, limit])
                pre = left
                limit = right
        result.append([pre, limit])
        
        return len(result)
# @lc code=end

