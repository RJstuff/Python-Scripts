from collections import defaultdict
class Graph :
    def __init__(self):
        self.graph = defaultdict(list)
    def edge(self,u,v) :
        self.graph[u].append(v)
    def bfs(self,s):
        visited = [False] * (len(self.graph))

        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end = " ")

            for i in self.graph[s] :
                if visited[i] == False :
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.edge(0,1)
g.edge(0,2)
g.edge(1,2)
g.edge(2,0)
g.edge(2,3)
g.edge(3,3)

print("following is breadth first traversal" + " ,starting from vertex 2")
g.bfs(2)
