#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   q2.py
@Time    :   2021/10/19 19:50:49
@Author  :   Tang Yujin 
@Version :   1.0
@Contact :   tangyujin0275@gmail.com
'''
# str1 = [int(n) for n in input().split()]
# dict = {}
# for i in range(0,str1[0]):
#     str = [int(n) for n in input().split()]
#     dict[str[0]]= str[1]
# 二维动态规划
# n, v = map(int, input().split())
# goods = []
# for i in range(n):
#     goods.append([int(i) for i in input().split()])

# # 初始化，先全部赋值为0，这样至少体积为0或者不选任何物品的时候是满足要求  
# dp = [[0 for i in range(v+1)] for j in range(n+1)]

# for i in range(1, n+1):
#     for j in range(1,v+1):
#         dp[i][j] = dp[i-1][j]  # 第i个物品不选
#         if j>=goods[i-1][0]:# 判断背包容量是不是大于第i件物品的体积
#             # 在选和不选的情况中选出最大值
#             dp[i][j] = max(dp[i][j], dp[i-1][j-goods[i-1][0]]+goods[i-1][1])


# print(dp[-1][-1])
# 一维动态优化
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

