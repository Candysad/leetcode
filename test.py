from itertools import accumulate
from functools import cache
from math import comb
from heapq import *

mod = 10 ** 9 + 7

@cache
def bin(n: int) -> int:
    result = 0
    while n != 1:
        result += 1
        n = n.bit_count()
    return result

def countKReducibleNumbers(s: str, k: int) -> int:
    n = len(s)
    if n == 1:
        return 0

    s = [1 if c == '1' else 0 for c in s]
    ones = list(accumulate(s, initial=0))
    def dfs(i: int) -> int:
        if s[i] == 0:
            return dfs(i + 1) % mod
        else:
            t = 0
            res = n - 1 - i
            for j in range(res + 1):
                if j == 0 and i == 0: continue
                tk = 1 if 1 + bin(j + ones[i]) <= k else 0
                t = (t + comb(n - 1 - i, j) * tk) % mod
            
            t = (t + dfs(i + 1)) % mod
            return t
    return dfs(0)

s = "1000"
k = 2
countKReducibleNumbers(s, k)
