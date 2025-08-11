#
# @lc app=leetcode.cn id=842 lang=python3
#
# [842] 将数组拆分成斐波那契序列
#

# @lc code=start
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        INT_MAX = 2**31 - 1
          
        n = len(num)
        if n < 3:
            return []
        
        def dfs(i, pre1, pre2):
            if i == n:
                return True
            target = pre1 + pre2
            if pre1 > INT_MAX or pre2 > INT_MAX or target > INT_MAX:
                return False
            
            if num[i] == '0' and target != 0:
                return False
            
            target = str(target)
            if n - i < len(target):
                return False
            
            for c in target:
                if c != num[i]:
                    return False
                i += 1
            
            target = pre1 + pre2
            result.append(target)
            return dfs(i, pre2, target)

        
        # 第一个是 0 
        if num[0] == '0':
            pre1 = 0
            if num[1] == '0':
                pre2 = 0
                result = [0, 0]
                t = dfs(2, 0, 0)
                if t:
                    return result
            else:
                for j in range(2, n):
                    pre2 = int(num[1:j])
                    result = [0, pre2]
                    t = dfs(j, 0, pre2)
                    if t:
                        return result
        

        for i in range(1, n-2):
            pre1 = int(num[0:i])
            # 第二个是 0
            if num[i] == '0':
                result = [pre1, 0]
                t = dfs(i+1, pre1, 0)
                if t:
                    return result
                continue
            
            for j in range(i+1, n):
                pre2 = int(num[i:j])
                result = [pre1, pre2]
                t = dfs(j, pre1, pre2)
                if t:
                    return result
        return []
# @lc code=end

