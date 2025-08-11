#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
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
    def intToRoman(self, num: int) -> str:
        def check(num: int):
            for key in charMap:
                if num >= charMap[key]:
                    return key, charMap[key]
        
        result = ''
        while num > 0:
            t, tt = check(num)
            result += t
            num -= tt
        
        return result
# @lc code=end

