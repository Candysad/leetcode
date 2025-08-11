#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
from collections import Counter
# @lc code=start
'''
异位词的id就是他的 hash
但其实对每个子串都单独算一遍hash不够快
因为前后两个候选子串只有一个字符不同，只用改一个地方
'''
# def hashstr(s:str):
    # shash = [0] * 26
    # for c in s:
    #     shash[ord(c) - ord("a")] += 1
    # return ' '.join([str(c) for c in shash])# 间隔符是需要的
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        手搓 hash
        '''
        # n = len(s)
        # length = len(p)
        # phash = [0] * 26
        # for c in p:
        #     phash[ord(c) - ord("a")] += 1
        # phash = ' '.join([str(c) for c in phash])# 间隔符是需要的
        
        # result = [-1]
        # shash = [0] * 26
        # for c in s[:length]: # 第一个子串的 hash
        #     shash[ord(c) - ord("a")] += 1
        # if " ".join([str(c) for c in shash]) == phash:
        #     result.append(0)
        
        # # 只需要遍历目标长度的子串就行了
        # # 第一个子串的 right下标是 length-1，这里从第二个开始遍历所以是 length
        # for right in range(length, n):
        #     left = right - length + 1
        #     if s[left-1] == s[right]:# 一样就不用改 hash
        #         if result[-1] == left-1: # 上一个是异位词
        #             result.append(left)
        #     else:
        #         # 变了，比一下
        #         shash[ord(s[left-1]) - ord("a")] -= 1 #把上一个左边去掉
        #         shash[ord(s[right]) - ord("a")] += 1 # 把下一个右边放进来
        #         if " ".join([str(c) for c in shash]) == phash:
        #             result.append(left)
        # return result[1:] # 把开头占位的-1丢掉
        
        '''
        用 Counter
        '''
        phash = Counter([c for c in p])
        n = len(s)
        length = len(p)
        shash = Counter([c for c in s[:length]])
        result = [-1, 0] if phash == shash else [-1]
        for left in range(1, n-length+1):
            if s[left-1] == s[left + length -1]:
                if result[-1] == left - 1:
                    result.append(left)
            else:
                shash[s[left-1]] -= 1
                shash[s[left + length -1]] += 1
                if phash == shash:
                    result.append(left)
        
        return result[1:]
        
        
# @lc code=end

