# KMP

```python
# 找第一个
def kmp(s: str, p: str) -> int:
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

```python
# 找全部
def kmp(s: str, p: str) -> List[int]:
    def get_next(p):
        n = len(p)
        next = [-1] * n

        for i in range(1, n):
            last = next[i-1]
            while last > -1 and p[last + 1] != p[i]:
                last = next[last]
            if p[last + 1] == p[i]:
                next[i] = last + 1
        return next

    next = get_next(p)
    sn, pn = len(s), len(p)
    i, j = 0, 0
    result = []
    while i < sn:
        if s[i] == p[j]:
            i += 1
            j += 1
            if j == pn:
                result.append(i - pn)
                j = next[j - 1] + 1
        else:
            if j == 0:
                i += 1
            else:
                j = next[j - 1] + 1
    return result
```



## [Z 函数](https://oi-wiki.org/string/z-func/) / 扩展 KMP

- 找出字符串 `s` 中每个下标开始的 `s` 的前缀的最大长度，形成数组 `z`
- 固定 `z[0] = 0`

```python
def zFunction(s: str):
    n = len(s)
    z = [0] * n
    left, right = 0, 0
    for i in range(1, n):
        # z[i] = max(0, min(z[i - left], right - i + 1))
        # Python 的 max 和 min 需要考虑类型，会比直接大小比较慢
        if i < right:
            _1 = z[i - left]
            _2 = right - i + 1
            z[i] = _1 if _1 < _2 else _2

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









