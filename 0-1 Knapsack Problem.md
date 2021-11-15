## 0-1 Knapsack Problem

### Solution Idea

Use a one-dimension matrix dp to store every volume's corresponding maximum value, dp[i], initialize the matrix with 0.

Use dynamic programming, Use double loops, if current volume could let in the item, then the correspongding dp[i] euqals the maximum of current value and the value of let in the current item.

### Time Complexity

O(mn) 

m-number of items

n-volume

### Space Complexity

O(m+n)

m-number of items

n-volume

### Python Code

```python
n, v = map(int, input().split())
goods = []
for i in range(n):
    goods.append([int(i) for i in input().split()])

dp = [0 for i in range(v+1)]

for i in range(n):
    for j in range(v,-1,-1): # 从后往前
        if j >= goods[i][0]:
            dp[j] = max(dp[j], dp[j-goods[i][0]] + goods[i][1])

print(dp[v])
```

