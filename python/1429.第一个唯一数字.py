#
# @lc app=leetcode.cn id=1429 lang=python3
#
# [1429] 第一个唯一数字
#
from collections import defaultdict, deque
# @lc code=start
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.counter = defaultdict(int)
        self.firsts = deque()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        counter, firsts = self.counter, self.firsts
        while firsts and counter[firsts[0]] != 1:
            firsts.popleft()
        if firsts:
            return firsts[0]
        return -1

    def add(self, value: int) -> None:
        counter, firsts = self.counter, self.firsts
        counter[value] += 1
        if counter[value] == 1:
            firsts.append(value)
# @lc code=end

