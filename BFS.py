from collections import deque

class Graph:
    def __init__(self, vertex):
        self.mat = [[0]*vertex for x in range(vertex)]
        self.size = vertex

    def addEdge(self, src, dest):
        if ( 0 <= src, self.size and 0 <= dest < self.size):
            self.mat[src][dest] = 1
            self.mat[src][dest] = 1
        else:
            print("Invalid Edge")

    def BFS(self, src):
        visited = [False] * self.size
        queue = deque([src])
        visited[src] = True

        while(queue):
            v = queue.popleft()
            print(v, end=" ")

            for i in range(self.size):
                if(self.mat[v][i] == 1 and visited[i] == False):
                    visited[i] = True
                    queue.append(i)

# Runner Code
g = Graph(8)
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,3)
g.addEdge(3,5)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(4,6)
g.addEdge(6,2)
g.addEdge(6,7)

g.BFS(0)