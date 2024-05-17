#
# @lc app=leetcode.cn id=386 lang=python3
#
# [386] 字典序排数
#

# @lc code=start
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        def dfs(i):
            result.append(i)
            
            if i * 10 <= n:
                dfs(i*10)
            
            if i % 10 < 9 and i + 1 <= n:
                dfs(i+1)
                
        dfs(1)
        return result
  
        # result = []
        # now = 1
        # for i in range(n):
        #     result.append(now)
            
        #     if now * 10 <= n:
        #         now *= 10
        #     else:
        #         while now == n or now % 10 == 9:
        #             now //= 10
        #         now += 1
        # return result
# @lc code=end

