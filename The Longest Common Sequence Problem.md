## The Longest Common Sequence Problem 

### Solution Idea

In this question, general idea requires a O(n2) time complexity, to spare time and consider the speciality(the numbers in sequence are not repeated), consider **transerfering the LCS question into a LIS question**. Use a dictionary to store the position of sequence A, find B's every item in A and return the correspongding position in A, we can get a new list.

Then computing the longest increasing subsequence of the new list, we can get the LCS of A and B.

About the detail of the LIS algorithm, please refer to the (4) question.

### Time Complexity

O(nlogn)

### Space Complexity

O(n)

### Python Code

```python
str1 = [int(n) for n in input().split()]
str2 = [int(n) for n in input().split()]
dict = {}
for i in range(len(str1)):
    # str1的key为当前position
    dict[str1[i]] = i
for i in range(len(str2)):
    # 找到str2在str1中重复的value，并把对应的在str1中的position赋给str2[i]，如果找不到。返回False
    str2[i] = dict[str2[i]]
# 转化为str2的最长上升子序列问题
def LIS(list):
    if list == []: 
        return 0
    length=len(list)
    # 暂存查找到的子序列
    dp=[1 for _ in range(length)]
    lis=0   # 增长子串的长度
    for n in list:
        # 利用二分查找法来搜索子序列
        left = 0
        right = lis
        while left<right:
            mid = (left + right)//2
            if dp[mid] < n:
                left = mid +  1
            else:
                right = mid           
        if left == lis: 
            lis += 1
        dp[left] = n           
    return lis
num = LIS(str2)
print(num)
```
