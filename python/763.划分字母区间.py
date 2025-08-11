#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        table = {}
        for i, c in enumerate(s):
            if c not in table:
                table[c] = [i, i]
            else:
                table[c][1] = i
        
        spans = sorted([table[key] for key in table])
        result = []
        
        last = spans[0]
        for s in spans[1:]:
            # 不会有相等，每个区间对应那个字母的下标，字母肯定不同
            # 而且排序了，只会 s[0] >= last[0]
            if s[0] < last[1]: # 交叉
                last[1] = max(last[1], s[1])
            else: # 分隔，前面可以自成一组
                result.append(last[1] - last[0] + 1)
                last = s
        
        result.append(last[1] - last[0] + 1)
        return result
# @lc code=end

