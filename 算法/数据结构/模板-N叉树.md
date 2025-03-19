# N 叉树

```python
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
```



### 序列化与反序列化

- 按照 LeetCode 风格进行编码

- 空树对应 `[]`

- ```python
  class Codec:
      def serialize(self, root: 'Node') -> str:
          if root is None:
              return '[]'
  
          result = []
          queue = [(root, 0)]
          max_fa = 1
          while queue:
              now = 0
              count = 0
              t = queue
              queue = []
  
              for node, fa in t:
                  while  fa != now:
                      now += 1
                      result.append("null")
                  
                  result.append(str(node.val))
                  for c in node.children:
                      queue.append((c, count))
                  count += 1
              
              while now < max_fa:
                  now += 1
                  result.append("null")
              max_fa = count
          
          while result and result[-1] == "null":
              result.pop()
          return ','.join(result)
  
      def deserialize(self, data: str) -> 'Node':
          if data == "[]":
              return None
          data = data.split(',')
          root = Node(-1)
          queue = deque([root])
          t = deque()
          for item in data:
              if item == 'null':
                  queue.popleft()
                  if not queue:
                      queue = t
                      t = deque()
              else:
                  num = int(item)
                  node = Node(num)
                  queue[0].children.append(node)
                  t.append(node)
          return root.children[0]
  ```
  
  

