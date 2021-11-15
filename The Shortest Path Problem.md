# The Shortest Path Problem

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

