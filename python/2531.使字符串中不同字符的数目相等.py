#
# @lc app=leetcode.cn id=2531 lang=python3
#
# [2531] 使字符串中不同字符的数目相等
#
from collections import Counter
# @lc code=start
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        '''
        O(n^2) 遍历
        '''
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        if len(counter1) > len(counter2):
            counter1, counter2 = counter2, counter1
        d = abs(len(counter1) - len(counter2))
        if d >= 3:
            return False
        
        for c1 in counter1:
            for c2 in counter2:
                if c1 == c2:
                    if d == 0:
                        return True

                else:
                    l1 = len(counter1) - (1 if counter1[c1] == 1 else 0) + (1 if counter1[c2] == 0 else 0)
                    l2 = len(counter2) - (1 if counter2[c2] == 1 else 0) + (1 if counter2[c1] == 0 else 0)
                    if l1 == l2: return True
                    
        return False
    
        '''
        O(n) 遍历
        '''
        # counter1 = Counter(word1)
        # counter2 = Counter(word2)
        
        # d = abs(len(counter1) - len(counter2))
        # if d >= 3:
        #     return False
        # if len(counter1) > len(counter2):
        #         counter1, counter2 = counter2, counter1
        
        # if d == 0:
        #     # 有多余1个的对方没有的字，交换
        #     c1UniqueOver1 = False
        #     c2UniqueOver1 = False
        #     # 有仅1个的对方没有的字， 交换
        #     c1Unique1 = False
        #     c2Unique1 = False
        #     # 都有同一个字，交换
        #     same = False
            
        #     for c1 in counter1:
        #         if counter2[c1]:
        #             same = True
        #         else:
        #             if counter1[c1] == 1:
        #                 c1Unique1 = True
        #             else:
        #                 c1UniqueOver1 = True
            
        #     for c2 in counter2:
        #         if counter1[c2] == 0:
        #             if counter2[c2] == 1:
        #                 c2Unique1 = True
        #             else:
        #                 c2UniqueOver1 = True
                
        #     return same or (c1Unique1 and c2Unique1) or (c1UniqueOver1 and c2UniqueOver1)

        # if d == 1:
        #     # 少的给对方没有自己多余的，多的给自己仅1个对方没有的，多的-1+1， 少的+1
        #     # 少的给对方有自己仅1个的，多的给自己仅1个对方没有的，少的-1+1， 多的-1
        #     # 少的给对方有自己多余的，多的给自己多余1个且少的没有的 少的+1
        #     # 少的给对方有自己多余的，多的给自己只有1个且少的有的 多的-1，少的不能把多的给过来的再给回来
        #     same1over1 = []
        #     same1Unique1 = False
        #     c1UniqueOver1 = False
            
        #     c2Unique1 = False
        #     c2UniqueOver1 = False
        #     same2Unique1 = []
            
        #     for c1 in counter1:
        #         if c1 not in counter2 and counter1[c1] > 1:
        #             c1UniqueOver1 = True
        #         if c1 in counter2 and counter1[c1] == 1:
        #             same1Unique1 = True
            
        #     for c2 in counter2:
        #         if counter1[c2]:
        #             if counter1[c2] > 1:
        #                 same1over1.append(c2)
        #             if counter2[c2] == 1:
        #                 same2Unique1.append(c2)
        #         else:
        #             if counter2[c2] > 1:
        #                 c2UniqueOver1 = True
        #             else:
        #                 c2Unique1 = True
            
        #     if (c1UniqueOver1 and c2Unique1) or (same1Unique1 and c2Unique1):
        #         return True
            
        #     if same1over1:
        #         if c2UniqueOver1:
        #             return True
        #         for c2 in same2Unique1:
        #             if counter1[c2] == 1 or len(same1over1) > 1:
        #                 return True
            
        #     return False
        
        # if d == 2:
        #     # 少的给对方有的自己多余1个的，多的给自己只有一个且少的没有的
        #     same1over1 = False
        #     c2Unique1 = False
            
        #     for c2 in counter2:
        #         if counter1[c2] > 1:
        #             same1over1 = True
                
        #         if counter1[c2] == 0 and counter2[c2] == 1:
        #             c2Unique1 = True
            
        #     return same1over1 and c2Unique1
# @lc code=end

