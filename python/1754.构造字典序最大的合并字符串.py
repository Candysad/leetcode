#
# @lc app=leetcode.cn id=1754 lang=python3
#
# [1754] 构造字典序最大的合并字符串
#

# @lc code=start
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        result = []
        m, n= len(word1), len(word2)
        p1, p2 = 0, 0
        
        while p1 < m and p2 < n:
            if word1[p1] < word2[p2]:
                result.append(word2[p2])
                p2 += 1
            elif word1[p1] > word2[p2]:
                result.append(word1[p1])
                p1 += 1
            else:
                if word1[p1:] >= word2[p2:]:
                    result.append(word1[p1])
                    p1 += 1
                else:
                    result.append(word2[p2])
                    p2 += 1
        result.append(word1[p1:])
        result.append(word2[p2:])
        return ''.join(result)
# @lc code=end