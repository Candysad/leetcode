#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#

# @lc code=start
'''
字典树
'''
# def add(trie:dict, s:list):
#     last = trie
#     for n in s:
#         _next = last.get(n, -1)
#         if _next == -1:
#             _next = {}
#             last[n] = _next
#         last = _next

# def find(trie:dict, s:list):
#     last = trie
#     result = 0
#     for n in s:
#         _next = last.get(n, -1)
#         if _next == -1:
#             return result
#         last = _next
#         result += 1
#     return result

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # trie = {}
        # for i in range(len(nums1)):
        #     add(trie, nums1[i:])
        
        # result = 0
        # for i in range(len(nums2)):
        #     t = find(trie, nums2[i:])
        #     result = max(t, result)
        
        # return result
        
        '''
        DP
        dp[i][j]表示 nums1[i] nums2[j] 及前面的最长公共长度
        nums1[i] == nums2[j] 才有公共，不然就是 0
        '''
        n = len(nums1)
        m = len(nums2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        
        result = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1] 
                    result = max(result, dp[i][j])
        
        return result
# @lc code=end

