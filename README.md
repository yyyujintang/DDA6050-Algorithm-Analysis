# DDA6050-Algorithm-Analysis

# A2_Report_221041014

## (1) The Longest Common Sequence Problem (15 points)

[q1.py](https://github.com/yyyujintang/DDA6050-Algorithm-Analysis/blob/main/q1.py)

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

## (2) 0-1 Knapsack Problem (15 points)

[q2.py](https://github.com/yyyujintang/DDA6050-Algorithm-Analysis/blob/main/q2.py)

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



## (3) The Shortest Path Problem (15 points)

[q3.py](https://github.com/yyyujintang/DDA6050-Algorithm-Analysis/blob/main/q3.py)

### Solution Idea

Using Dijkstra method to solve the shortest path problem. Use matrix dis to store the path length, 

Fisrt initialize single source path to 0 and others remain infinite(in the program using 1000000000000). 

And then build a min-heap, push all edges from start to any other vertice, pop the minimal edge. If the vertice is poped, then stop relaxing. Record the pop vertice(use visit list to record, 1 present popped)

And then relax the edge, push new wieght to the heap and update the matrix dis

### Time Complexity

O(VlogV+ElogV)=O(ElogV)

V:the number of vertices

E:the number of edges

### Space Complexity

O(E+V)

V:the number of vertices

E:the number of edges

### Python Code

```python
import heapq
class graph:
    def __init__(self,num,ma):
        self.edge={}
        self.dic=[ma]*(num+1)
    def add(self,u,v,w):
        if u in self.edge:
            self.edge[u].append((v,w))
        else:
            self.edge[u]=[(v,w)]
    def dijkstra(self,start,target):
        dis=self.dic
        dis[start]=0
        heap=[]
        visit=[0 for i in range(len(dis))]
        for i in self.edge[start]:
            dis[i[0]]=i[1]
            heapq.heappush(heap,(i[1],i[0]))# i[1]为该边权值，i[0]为该点，从start点到其余点的边入堆
        while heap!=[]:
            vic=heapq.heappop(heap)# 弹出最小边
            if visit[vic[1]]==1:# 如果该点已经弹出过，则不再松弛
                continue
            visit[vic[1]] = 1# 记录弹出点
            if vic[1] not in self.edge:# 防止有向图中出度为0的点
                continue
            for i in self.edge[vic[1]]:
                if dis[i[0]]>dis[vic[1]]+i[1]:# 判断是否松弛
                    dis[i[0]]=dis[vic[1]]+i[1]# 松弛边
                    heapq.heappush(heap,(i[1],i[0]))# 松弛过边则把新边权值入堆
        self.dic=dis
        return self.dic[target]
if __name__ == "__main__":
    N,M,s,t = map(int, input().split())
    g=graph(N,1000000000000)
    for i in range(M):
        G = ([int(i) for i in input().split()])
        g.add(G[0],G[1],G[2])
    # g.dijkstra(1)
    print(g.dijkstra(s,t))
```



## (4)The Longest Increasing Subsequence Problem (25 points)

[q4.py](https://github.com/yyyujintang/DDA6050-Algorithm-Analysis/blob/main/q4.py)

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



##  (5)Max M Sum Subsequences Problem (30 points)

[q5.py](https://github.com/yyyujintang/DDA6050-Algorithm-Analysis/blob/main/q5.py)

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

