#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#
from collections import Counter
# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        sn = len(s)
        n = len(words)
        wn = len(words[0])
        target = Counter(words)
        result = []
        
        for start in range(wn):
            left = start
            right = start + n * wn
            if right > sn:
                break

            window = s[left: right]
            hashwindow = Counter([window[i * wn : (i+1) * wn] for i in range(n)])
            if hashwindow == target:
                    result.append(left)
            
            while right <= sn - wn:
                hashwindow[ s[left : left + wn] ] -= 1
                hashwindow[ s[right: right + wn] ] += 1
                left += wn
                right += wn
                if hashwindow == target:
                    result.append(left)
                
        return result            
# @lc code=end

