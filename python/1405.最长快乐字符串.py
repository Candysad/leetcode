#
# @lc app=leetcode.cn id=1405 lang=python3
#
# [1405] 最长快乐字符串
#
# @lc code=start
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        t = [[a, 'a'], [b, 'b'], [c, 'c']]
        t.sort(key=lambda x: x[0], reverse=True)
        result = []
        while t[0][0] > 0:
            if t[1][0] == 0:
                if result and result[-1][-1] == t[0][1]:
                    return ''.join(result)
                else:
                    result.append(t[0][1]*min(2, t[0][0]))
                    return ''.join(result)
            
            elif t[0][0] == t[1][0]:
                n = min(2, t[0][0])
                result.append((t[0][1]+t[1][1]) * n)
                t[0][0] -= n
                t[1][0] -= n
            
            else:
                result.append(t[0][1]*2 + t[1][1])
                t[0][0] -= 2
                t[1][0] -= 1
            
            t.sort(key=lambda x: x[0], reverse=True)
        
        return ''.join(result)
# @lc code=end

