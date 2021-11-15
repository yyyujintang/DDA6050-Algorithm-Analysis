##  Max M Sum Subsequences Problem

### Solution Idea

Use two one-dimension matrix to store the current maximum.

The key idea of the solution is that, for current number j, it's the first number of the subsequence i. Or it's note the first number of the subqequence.

Use two one-dimension matrix dp and mk to store the max sum. **This could reduce the space complexity.**

dp[j] means j in current subsequence's(j is the first number) maximal sum, mk[j] means j in last subsequence's(j is not the first number)  maximum sum.

If j is the fisrt number, then :
$$
dp[j] = mk[j-1]+num[j]
$$
If j is not the first number, thenthe transition quation:
$$
dp[j] = max(dp[j-1] + num[j] ,mk[j-1]+num[j])
$$

### Time Complexity

O(mn)

m: the number of subsequence

n: the length of the list

### Space Complexity

0(n)

### Python Code

```python
n,m = [int(n) for n in input().split()]
list = [int(n) for n in input().split()]
INF=999

dp = [0] * n 
mk = [0] * n
for i in range(m): #枚举子序列
    Max = - INF
    for j in range(i,n):
        if(i == j):
           dp[j] = mk[j-1] + list[j]#第i个元素只能是第i个子序列的第一个
        else:
           dp[j] = max(dp[j-1] ,mk[j-1]) + list[j]
           mk[j-1] = Max 
        if(Max < dp[j]): 
            Max = dp[j]
print(Max)
```

