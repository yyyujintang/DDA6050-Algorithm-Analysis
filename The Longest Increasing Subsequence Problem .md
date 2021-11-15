## The Longest Increasing Subsequence Problem 

### Solution Idea

In this question, I use a one-dimension matrix dp to store the seached sub list, and use 1 to initialize the matrix.

For all items in list, use binary search method to decide whether to add an item into a list, use two  location parameter, left and right to decide the rising sublist, erverytime reset left to zero, and set right as current longest sub list length.

### Time Complexity

O(nlogn)

### Space Complexity

O(n)

### Python Code

```python
str1 = [int(n) for n in input().split()]
str2 = [int(n) for n in input().split()]
def LIS(list):
    # 如果列表为空，返回0
    if list == []: 
        return 0
    length=len(list)
    # 用一维矩阵dp暂存查找到的子序列，用1进行初始化
    dp=[1 for _ in range(length)]
    lis=0   # 增长子串的长度
    for item in list:# 0(N)
        # 利用二分查找法来搜索子序列，设置两个位置参数left和right
        left = 0 # 每次把左边设置为0
        right = lis #右边作为当前最长子串长度
        while left<right: # 当左边小于右边时，进行logN次查找
            mid = (left + right)//2
            if dp[mid] < item:# 二分查找：中间值小于item，在左半区间中进行查找；否则，在右半区间中进行查找
                left = mid +  1
            else:
                right = mid           
        if left == lis: # 查找结束，如果left=lis，子串长度+1
            lis += 1
        dp[left] = item  # 把查找到的当前元素加到子序列里的对应位置中          
    return lis,dp
num ,dp = LIS(str2)
print(num,dp)
```

