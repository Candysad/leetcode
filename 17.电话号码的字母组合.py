#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        '''
        遍历
        '''
        # result = []
        # for d in digits:
        #     if result:
        #         t = [r+p for r in result for p in phoneMap[d]]
        #         result = t
        #     else:
        #         for c in phoneMap[d]:
        #             result.append(c)
        # return result
        
        '''
        递归
        '''
        def backtrack(index: int):
            if index == len(digits): # 到头了则添加一组
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]: # 没到头则循环递归添加一个字符
                    combination.append(letter)
                    backtrack(index + 1) # 递归添加下一个可能的字符
                    combination.pop() # 递归到头后再到这一步，回退一个字符准备换成下一个

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations 
# @lc code=end

