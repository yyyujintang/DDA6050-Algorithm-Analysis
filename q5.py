n,m = [int(n) for n in input().split()]
list = [int(n) for n in input().split()]
INF=999

dp = [0] * n 
pre = [0] * n
# for i in range(m): #枚举子序列
#     Max = - INF
#     for j in range(n):
#        if(i == j):
#            dp[j] = mk[j-1] + list[j]#第i个元素只能是第i个子序列的第一个
#        else:
#            dp[j] = max(dp[j-1] ,mk[j-1]) + list[j]
#            mk[j-1] = Max #这个地方注意了，不能更新mk[j]，只能更新j-1因为更新j就会被当前的这个子序列更新的时候用到。
#     #    if(Max < dp[j]): 
#     #        Max = dp[j]
for i in range(m): #枚举子序列
    Max = - INF
    for j in range(i,n):
        dp[j] = max(dp[j-1] ,pre[j-1]) + list[j]
        pre[j-1] = Max
        Max = max(Max,dp[j]) #
print(Max)
