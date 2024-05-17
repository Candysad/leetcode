#
# @lc app=leetcode.cn id=2071 lang=python3
#
# [2071] 你可以安排的最多任务数目
#
from bisect import bisect_left
# @lc code=start
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        '''
        只能从多到少从大到小比较 taskc 个最轻松的工作能不能做完
        减少比较次数所以用二分来确定每次比较多少个工作
        '''
        n = len(tasks)
        m = len(workers)
        tasks.sort()
        workers.sort()
        
        def check(taskc):
            p = pills
            inwork = workers[m - taskc:]
            
            for job in tasks[taskc-1 :: -1]:
                if inwork[-1] >= job:
                    inwork.pop()
                else:
                    if p == 0 or inwork[-1] + strength < job:
                        return False

                    might = bisect_left(inwork, job-strength)
                    p -= 1
                    inwork.pop(might)
            
            return True

        result = 0
        left, right = 1, min(n, m)
        while left <= right:
            mid = (left+right)//2
            if check(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result
# @lc code=end

