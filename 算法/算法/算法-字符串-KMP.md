# KMP

```python
def strStr(s: str, p: str) -> int:
    def get_next(p):
        n = len(p)
        next = [-1] * n

        for i in range(1, n):
            last = next[i-1]
            while last > -1 and p[last+1] != p[i]:
                last = next[last]
            if p[last + 1] == p[i]:
                next[i] = last + 1
        return next

    next = get_next(p)
    sn = len(s)
    pn = len(p)
    i, j = 0, 0
    while i < sn:
        if s[i] == p[j]: # 正常匹配
            i += 1
            j += 1
            if j == pn:
                return i - pn
        else:
            if j == 0: # 第一个就没匹配上，s 向后走一个
                i += 1
            else: # 有匹配上一部分
                j = next[j - 1] + 1

    return -1
```

- 记录之前遍历的信息
- 通过记录的信息回退，减少遍历次数
- pattern 比 s 短，在pattern 上回退
- 回退信息来自之前匹配过的内容与后侧重复的内容，都是从前向后的顺序
- 默认一开始的 next[0]  为 0，没有必要使用
- next[i] 指出当前位置出错时应该按照之前的重复长度回退到哪个位置



## [Z 函数](https://oi-wiki.org/string/z-func/) / 扩展 KMP

```python
def zFunction(s: str):
    n = len(s)
    z = [0] * n
    left, right = 0, 0
    for i in range(1, n):
        z[i] = max(0, min(z[i - left], right - i + 1))

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > right:
            left = i
            right = i + z[i] - 1
    return z
```

- [demo](https://personal.utdallas.edu/~besp/demo/John2010/z-algorithm.htm)
- 记录最右的前缀区间，利用该区间来更新下一个下标位置



## 例题

- 28.[KMP](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/)
- 2223.[Z 函数](https://leetcode.cn/problems/sum-of-scores-of-built-strings/description/)









