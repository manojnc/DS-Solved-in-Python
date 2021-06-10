import numpy as np

class graph_ADT:

    def __init__(self,vertices):
        self._vertices = vertices
        self.adjMatrix = np.zeros((vertices,vertices))
        self._visited = [0] * self._vertices

    def insertEdge(self,u,v,x=1):
        self.adjMatrix[u][v] = x

    def removeEdge(self,u,v):
        self.adjMatrix[u][v] = 0

    def existEdge(self,u,v):
        return self.adjMatrix[u][v] != 0

    def vertexCount(self):
        return self._vertices

    def edgeCount(self):
        count = 0
        for i in range(0,self._vertices):
            for j in range(0,self._vertices):
                if self.adjMatrix[i][j] != 0:
                    count += 1
        return count

    def vertices(self):
        for i in range(self._vertices):
            print(i,end=' ')
        print()

    def edges(self):
        for i in range(self._vertices):
            print(i,end='==>')
            for j in range(self._vertices):
                if self.adjMatrix[i][j] != 0:
                    print(i,"--",j,end=',')
            print()

    def outDegree(self,u):
        count = 0
        for i in range(self._vertices):
            if self.adjMatrix[u][i] != 0:
                count += 1
        return count

    def inDegree(self,v):
        count = 0
        for i in range(self._vertices):
            if self.adjMatrix[i][v] != 0:
                count += 1
        return count

    def display(self):
        print(self.adjMatrix)

    def bfs(self,s):
        i = s
        visited = [0] * self._vertices
        q = []
        print(i,end=' ')
        q.append(i)
        visited[i] = 1
        while len(q) > 0:
            i = q.pop(0)
            for j in range(self._vertices):
                if self.adjMatrix[i][j] != 0 and visited[j] == 0:
                    print(j,end=" ")
                    visited[j] = 1
                    q.append(j)

    def dfs(self,s):
        if self._visited[s] == 0:
            print(s,end=' ')
            self._visited[s] = 1
            for j in range(self._vertices):
                if self.adjMatrix[s][j] == 1 and self._visited[j] == 0:
                    self.dfs(j)




G_undirected=graph_ADT(4)
G_undirected.display()
print(G_undirected.vertexCount())
print(G_undirected.edgeCount())
G_undirected.insertEdge(0,1)
G_undirected.insertEdge(0,2)
G_undirected.insertEdge(1,0)
G_undirected.insertEdge(1,2)
G_undirected.insertEdge(2,0)
G_undirected.insertEdge(2,1)
G_undirected.insertEdge(2,3)
G_undirected.insertEdge(3,2)
G_undirected.display()
print(G_undirected.edgeCount())
print(G_undirected.existEdge(2,3))
G_undirected.removeEdge(2,3)
print(G_undirected.existEdge(2,3))
G_undirected.display()
print(G_undirected.edgeCount())

# directed and weighted

G=graph_ADT(4)
G.insertEdge(0,1,26)
G.insertEdge(0,2,16)
G.insertEdge(1,2,12)
G.insertEdge(2,3,8)
G.display()
print(G.edges())
print("in degree of 2 : ",G.inDegree(2))
print(G.existEdge(2,3))
#G.bfs(0)

## BFS demo

G_bfs = graph_ADT(7)
G_bfs.insertEdge(0,1)
G_bfs.insertEdge(0,5)
G_bfs.insertEdge(0,6)
G_bfs.insertEdge(1,0)
G_bfs.insertEdge(1,2)
G_bfs.insertEdge(1,5)
G_bfs.insertEdge(1,6)
G_bfs.insertEdge(2,3)
G_bfs.insertEdge(2,4)
G_bfs.insertEdge(2,6)
G_bfs.insertEdge(3,4)
G_bfs.insertEdge(4,2)
G_bfs.insertEdge(5,2)
G_bfs.insertEdge(5,3)
G_bfs.insertEdge(6,3)
print("bfs[0]")
G_bfs.bfs(0)
print()
print("dfs[0]")
G_bfs.dfs(0)
print()
print("bfs(4)")
G_bfs.bfs(4)
print()
print("dfs(4)")
G_bfs.dfs(4)
print()
print("bfs(1)")
G_bfs.bfs(1)
print()
print("dfs(1)")
G_bfs.dfs(1)
print()

G2=graph_ADT(7)
G2.insertEdge(0,1)
G2.insertEdge(0,5)
G2.insertEdge(0,6)
G2.insertEdge(1,0)
G2.insertEdge(1,2)
G2.insertEdge(1,5)
G2.insertEdge(1,6)
G2.insertEdge(2,3)
G2.insertEdge(2,4)
G2.insertEdge(2,6)
G2.insertEdge(3,4)
G2.insertEdge(4,2)
G2.insertEdge(4,5)
G2.insertEdge(5,2)
G2.insertEdge(5,3)
G2.insertEdge(6,3)
print("DFS")
G2.dfs(1)













