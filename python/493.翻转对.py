#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        vis = set()
        for num in nums:
            vis.add(num)
            vis.add(num // 2 if num % 2 else num // 2 - 1)
        
        vis = sorted(list(vis))
        table = {num : i+1 for i, num in enumerate(vis)}
        
        n = len(vis)
        fens = [0] * (n+1)
        def lowerbit(i):
            return i & -i

        def update(i, delta):
            while i <= n:
                fens[i] += delta
                i += lowerbit(i)
        
        def get(i):
            result = 0
            while i:
                result += fens[i]
                i -= lowerbit(i)
            return result

        result = 0
        for num in nums[::-1]:
            i = table[num // 2 if num % 2 else num // 2 - 1]
            result += get(i)
            i = table[num]
            update(i, 1)
        return result
# @lc code=end

