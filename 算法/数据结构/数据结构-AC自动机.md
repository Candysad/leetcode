### [Aho-Corasick automaton](https://leetcode.cn/link/?target=https%3A%2F%2Foi-wiki.org%2Fstring%2Fac-automaton%2F)

- 本质上是 字典树 + KMP

```python
tree = {}
def add(word):
    now = tree
    for c in word:
        next = now.get(c, {})
        now[c] = next
        now = next

def build_fail():
    tree[0] = 0 # deepth
    queue = []
    for c in range(26):
        c = chr(ord('a') + c)
        if c not in tree:
            tree[c] = tree
        else:
            tree[c][-1] = tree # fail
            queue.append(tree[c])

    deep = 1
    while queue:
        t = queue
        queue = []
        for node in t:
            node[0] = deep
            for c in range(26):
                c = chr(ord('a') + c)
                if c not in node:
                    node[c] = node[-1][c]
                else:
                    node[c][-1] = node[-1][c]
                    queue.append(node[c])
        deep += 1
```



### 例题

- 3291.[最少前缀构建目标](https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-i/)
- 3213.[额外属性的AC自动机](https://leetcode.cn/problems/construct-string-with-minimum-cost/)

