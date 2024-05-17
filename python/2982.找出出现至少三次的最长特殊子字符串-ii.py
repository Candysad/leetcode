#
# @lc app=leetcode.cn id=2982 lang=python3
#
# [2982] 找出出现至少三次的最长特殊子字符串 II
#

# @lc code=start
class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        table = {chr(ord('a')+ i): {"max":0} for i in range(26)} 
        # 统计每个字母的特殊字符串出现次数
        # max 存当前字母的最长特殊子串的长度
        
        # 滑动窗口找所有特殊子串
        left, right = 0, 0
        while left < n:
            while right < n and s[right] == s[left]:
                right += 1
            t = right - left
            
            _max = table[s[left]]["max"] + 1
            for i in range(_max, t+1): # 遍历增加统计到的所有特殊字串个数
                c = t-i+1 # 长度为 t 的特殊字串内长度为 i 的子串的个数，C_{t-i+1}^1
                if i not in table[s[left]]:
                    table[s[left]][i] = c
                else:
                    table[s[left]][i] += c
                # 满足要求则更新最长的
                if table[s[left]][i] >= 3:
                    table[s[left]]["max"] = i
        
            left = right
        
        result = 0
        for key in table:
            for key in table:
                result = max(result, table[key]['max'])
        return result if result else -1
# @lc code=end

