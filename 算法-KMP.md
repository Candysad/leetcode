# KMP 算法

```python
def strStr(self, s: str, pattern: str) -> int:
    def build_next(pattern: str):
        next = [0] # 开头默认为0
        i = 1 # 第一个已知，从第二个开始匹配前后缀
        prefix_len = 0
        while i < len(pattern):
            if pattern[prefix_len] == pattern[i]: # 当前前缀末尾和后缀末尾相同
                prefix_len += 1
                i += 1
                next.append(prefix_len)
            else:
                if prefix_len == 0: # 在和最开始匹配都没匹配上，没有相同前后缀
                    i += 1 #没匹配上，直接往后走
                    next.append(0)
                else:
                    prefix_len = next[prefix_len - 1] # 没匹配上，但是可以找以前的位置提前后移
                    								  # next 本身的构建也遵循回退
        return next

    next = build_next(pattern)
    # print(next)
    i = 0
    j = 0
    while i < len(s):
        # print(i,j)
        if s[i] == pattern[j]: # 相同，向后匹配
            i += 1
            j += 1
        elif j > 0: # 不相同但有重复
            j = next[j - 1] # 回退
        else:
            i += 1 # 没有重复，此时pattern匹配位置还在0，s 直接从下一个开始匹配
        if j == len(pattern): #pattern 匹配完，得到结果
            return i - j 返回当前s匹配结束位置减去 pattern 长度，得到 s 中匹配开始位置

    return -1
```

- 记录之前遍历的信息
- 通过记录的信息回退，减少遍历次数





### 之前遍历信息 next 数组

- pattern 比 s 短，在pattern 上回退
- 回退信息来自之前匹配过的内容与后侧重复的内容，都是从前向后的顺序
- 默认一开始的 next[0]  为 0，没有必要使用
- next[i] 指出当前位置出错时应该按照之前的重复长度回退到哪个位置





















