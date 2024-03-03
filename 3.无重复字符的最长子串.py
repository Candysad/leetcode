#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 1
        left = 0
        right = 1
        # 左右指针
        
        # 特殊情况
        if len(s) == 0:
            return 0
        
        while right < len(s):
            for i in range(left, right):
                if s[i] == s[right]: # 重复，挪左指针
                    left = i+1
                    break

            right+=1
            # 更新长度
            t = right - left
            length = t if t > length else length

        return length
            
# @lc code=end

