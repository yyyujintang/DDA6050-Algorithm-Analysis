#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   q3.py
@Time    :   2021/10/24 22:46:27
@Author  :   Tang Yujin 
@Version :   1.0
@Contact :   tangyujin0275@gmail.com
'''
# goods是一个二维矩阵，里面含有M个List，每一个List里面是一个三元组，代表两个点和一个距离

# Bellman-Ford核心算法
# 对于一个包含n个顶点，m条边的图, 计算源点到任意点的最短距离
# 循环n-1轮，每轮对m条边进行一次松弛操作

# 定理：
# 在一个含有n个顶点的图中，任意两点之间的最短路径最多包含n-1条边
# 最短路径肯定是一个不包含回路的简单路径（回路包括正权回路与负权回路）
# 1. 如果最短路径中包含正权回路，则去掉这个回路，一定可以得到更短的路径
# 2. 如果最短路径中包含负权回路，则每多走一次这个回路，路径更短，则不存在最短路径
# 因此最短路径肯定是一个不包含回路的简单路径，即最多包含n-1条边，所以进行n-1次松弛即可

# class CycleError(Exception):
#     pass
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
