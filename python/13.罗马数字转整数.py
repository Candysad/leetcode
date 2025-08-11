#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
charMap = {
            'M' : 1000,
            'CM': 900,
            'D' : 500,
            'CD': 400,
            'C' : 100,
            'XC': 90,
            'L' : 50,
            'XL': 40,
            'X' : 10,
            'IX': 9,
            'V' : 5,
            'IV': 4,
            'I' : 1,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        index = len(s) - 1
        result = 0
        while index >= 0:
            t = s[index]
            if index > 0 and t != 'I' and s[index-1 : index+1] in charMap.keys():
                result += charMap[s[index-1 : index+1]]
                index -= 2
            else:
                result += charMap[s[index]]
                index -=1 
        
        return result
        
# @lc code=end

