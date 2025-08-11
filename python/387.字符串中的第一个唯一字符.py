#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 记一遍出现次数
        # 再找一遍第一个个数为1的
        # 再找他在序列里的位置
        pre = {}
        for c in s:
            if c not in pre:
                pre[c] = 1
            else:
                pre[c] += 1
        
        for key in pre:
            if pre[key] == 1:
                return s.index(key)
        return -1
# @lc code=end

