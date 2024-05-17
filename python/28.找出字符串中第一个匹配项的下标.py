#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        暴力
        '''
        # for i in range(0, len(haystack)):
        #     if haystack[i:len(needle)+i] == needle:
        #         return i
        # return -1
    
        '''
        KMP
        '''
        def build_next(pattern: str):
            next = [0] # 开头默认为0
            i = 1 # 第一个已知，从第二个开始匹配前后缀
            prefix_len = 0
            while i < len(pattern):
                if pattern[prefix_len] == pattern[i]:
                    prefix_len += 1
                    i += 1
                    next.append(prefix_len)
                else:
                    if prefix_len == 0: # 在和最开始匹配都没匹配上，没有相同前后缀
                        i += 1 #没匹配上，直接往后走
                        next.append(0)
                    else:
                        prefix_len = next[prefix_len - 1] # 没匹配上，但是可以找以前的位置提前后移
            return next

        next = build_next(needle)
        # print(next)
        i = 0
        j = 0
        while i < len(haystack):
            # print(i,j)
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j > 0:
                j = next[j - 1]
            else:
                i += 1
            if j == len(needle):
                return i - j
        
        return -1
# @lc code=end

