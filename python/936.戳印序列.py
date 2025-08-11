#
# @lc app=leetcode.cn id=936 lang=python3
#
# [936] 戳印序列
#

# @lc code=start
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        '''
        逆向思维
        '''
        
        n = len(stamp)
        nt = len(target)
        if nt > 10 * nt * n:
            return []
        
        mark = [0] * nt # 0 不为 ？； 1 是 ?
        def check(i):
            if i+n > nt:
                return False
            
            if all(mark[i:i+n]):
                return False
            
            for j in range(n):
                if stamp[j] != target[i+j] and mark[i+j] == 0:
                    return False
            return True

        queue = []
        vis = set()
        for i in range(nt - n + 1):
            if check(i):
                queue.append(i)
                vis.add(i)

        result = []
        while queue:
            t = queue
            queue = []

            for start in t:
                result.append(start)
                for j in range(n):
                    mark[start + j] = 1
            
            for i in range(nt - n + 1):
                if i not in vis and check(i):
                    queue.append(i)

        return result[::-1] if all(mark) else [] 
# @lc code=end

