# [Manacher](https://oi-wiki.org/string/manacher/)

```python
from typing import List

def manacher(s:str, spacial_token='#') -> List[int]:
    # 使用 `#` 插入字符串
    s = spacial_token + spacial_token.join(list(s)) + spacial_token
    
    n = len(s)
    r = [1] * n
    left, right = 0, -1
    for i in range(n):
        radius = 1 if i > right else min(r[left + right - i], right - i + 1)
        while i >= radius and i + radius < n and s[i - radius] == s[i + radius]:
            radius += 1
        r[i] = radius
        if i + radius - 1 > right:
            left = i - radius + 1
            right = i + radius - 1
    
    return r # 结果是基于 `#` 插入后的字符串
```



- 用 $d_1[i]$ 表示下标为 $i$ 的字符为中心（回文长度为奇数）能形成的最长回文的半径

- 用 $d_2[i]$ 表示下标为 $i$ 的字符为中心右侧（回文长度为偶数数）能形成的最长回文的半径
  $$
  a\ \overbrace{b\ a\ \underset{s_3}{b}\ a\ b}^{d_1[3]=3}\ c\\\\
  
  c\ \overbrace{b\ a\ \underset{s_3}{a}\ b}^{d_2[3]=2}\ d
  $$

- 维护当前已知的右侧最远的回文子字符串的范围 $[left, right]$

- 对于当前遍历到的第 $i$ 个位置

  - 其左侧字符已经作为中心点遍历过了
  - 若其仍在 $[left, right]$ 则其在 $[left, right]$ 中的对称点已经遍历过了
  - $[left, right]$ 为回文，可以用 $i$ 在这一段中的对称点更新它的回文半径
  - 更新时，可能对称点的半径在 $i$ 处会超出 $right$，对于超出的部分，因为还未遍历过，所以是未知的，即更新位置不能超出 $right$
    - $d_1[i] = \min(d_1[left + right - i], right - i + 1)$
    - $d_2[i]$ 类似
  - 更新后，继续向外侧遍历拓宽 $d_1[i]$，直到不再是回文或抵达边界
  - 拓宽后，根据当前 $i$ 和其半径更新 $left$ 和 $right$

- 进一步的，可以用特殊字符插入原有的所有字符间

  ```python
  spacial_token = '#'
  s = spacial_token + spacial_token.join(list(s)) + spacial_token
  ```

  - 使得 $d_2$ 变为以特殊字符为中心的奇数长度回文的半径
  - 处理有无问题是可以直接使用
  - 处理具体长度问题时，还需要半径长度删去特殊字符



- [最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/)
- [分隔回文子串](https://leetcode.cn/problems/palindrome-partitioning-iv/description/)
- [2472. 不重叠回文子字符串的最大数目](https://leetcode.cn/problems/maximum-number-of-non-overlapping-palindrome-substrings/description/)
- [214.最短开头回文](https://leetcode.cn/problems/shortest-palindrome/)



```java
public List<Integer> manacher(String s) {
    String special = "#";
    s = String.join(special, s.split("")) + special;

    List<Integer> r = new ArrayList<>(Collections.nCopies(s.length(), 1));

    int left = 0, right = -1;
    for (int i = 0; i < s.length(); i++) {
        int radius = i > right ? 1 : Math.min(r.get(left + right - i), right - i + 1);

        while (i >= radius && i + radius < s.length() && s.charAt(i - radius) == s.charAt(i + radius)) radius++;

        r.set(i, radius);
        if (i + radius - 1 > right) {
            left = i - radius + 1;
            right = i + radius - 1;
        }
    }
    return r;
}
```

