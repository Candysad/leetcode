from typing import List, Tuple
import json

# s = "aabaaaab"
# rk = [3, 5, 7, 0, 1, 2, 4, 6]
# sa = [3, 4, 5, 0, 6, 1, 7, 2]
# print(s, rk, sa)

# def height(s: str, rk: List[int], sa: List[int]) -> List[int]:
#     n = len(s)
#     h = [0] * n
#     k = 0
#     for i in range(n):
#         if k: k -= 1
#         j = sa[rk[i] - 1]
#         while i + k < n and j + k < n and s[i + k] == s[j + k]:
#             k += 1 
#         h[rk[i]] = k
#     return h

# print(height(s, rk, sa))

s = "aabaaaab"
rk = [4, 6, 8, 1, 2, 3, 5, 7]
sa = [4, 5, 6, 1, 7, 2, 8, 3]
print(s, rk, sa)

def height(s: str, rk: List[int], sa: List[int]) -> List[int]:
    n = len(s)
    h = [0] * n
    k = 0
    for i in range(n):
        if k: k -= 1
        j = sa[rk[i] - 1 - 1] - 1
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1 
        h[rk[i] - 1] = k
    return h

print(height(s, rk, sa))