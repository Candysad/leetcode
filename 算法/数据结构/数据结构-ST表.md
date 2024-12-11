## ST 表

sparse-table

- 提前用 $O(n \log n)$ 时间维护单点长度为 $2^j$ 的表，使得单次查询时间降到 $O(1)$
- 本质上是下标为 起始位置 和 单点长度（$2^j$）的线段树，但维护好后不可修改



### 有向树上第 k 个祖先

```Python
def build(n: int, parent: List[int]):
    m = n.bit_length()
    tree = [[-1] * (m + 1) for _ in range(n)]
    for i, p in enumerate(parent):
        tree[i][0] = p
    for j in range(m):
        for i in range(n):
            p = tree[i][j]
            if p != -1:
                tree[i][j + 1] = tree[p][j]
    return tree

def find(tree: List[List[int]], node: int, k: int) -> int:
    for i in range(k.bit_length()):
        if (k >> i) & 1:
            node = tree[node][i]
            if node == -1:
                return node
    return node
```

 

### 区间最值

```python
def f(a, b):
    return max(a, b)

def build(nums: List[int]):
    n = len(nums)
    m = n.bit_length()
    tree = [[-1] * (m + 1) for _ in range(n)]
    
    for i in range(n):
        tree[i][0] = nums[i]
    for j in range(m):
        for left in range(n):
            mid = left + (1 << j)
            if mid >= n:
                break
            tree[left][j + 1] = f(tree[left][j], tree[mid][j])

    return tree

def find(tree, left: int, right: int):
    n = right - left
    m = n.bit_length() - 1
    mid = right - (1 << m) + 1
    return f(tree[left][m], tree[mid][m])
```

