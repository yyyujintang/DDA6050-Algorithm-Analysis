# str1 = [str(n) for n in input().split()]
# str2 = [str(n) for n in input().split()]
# # str1 = list(map(str,input.split()))
# # str2 = list(map(str,input.split()))

# def LCS(str1,str2):
#     m,n = len(str1),len(str2)
#     # 构建DP Table和Base Case
#     dp = [[0]*(n+1)for _ in range(m+1)]
#     # 进行状态转移
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             if str1[i-1]==str2[j-1]:
#                 # 找到一个LCS中的字符
#                 dp[i][j] = dp[i-1][j-1]+1
#             else:
#                 dp[i][j] = max(dp[i-1][j],dp[i][j-1])
#     return dp[-1][-1]
# lcs = LCS(str1,str2)
# # print(str1)
# print (lcs)
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