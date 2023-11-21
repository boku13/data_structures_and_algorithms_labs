class Graph():
    def __init__(self):
        self.vertices = {}
        self.edges = []
        
    def create_graph(self, v, e):
        for i in v:
            self.vertices[i] = []
            
        self.edges = e
        for i in e:
            # v[e[0]] = e[1]
            self.vertices[i[0]].append(i[1])
                    
    def print_graph(self):
        print(self.vertices.values())
        for v, e in self.vertices.items():
            print(v, e)
        print(self.vertices)
        
    def reachable_nodes(self, c):
        return self.bfs(c)
    
    def rendezvous_nodes(self, a, b):
        va = self.visited_bfs(a)
        vb = self.visited_bfs(b)
        
        print(va[0])
        print(va[1])
        print(vb[0])
        print(vb[1])
        # print(va)
        # print(vb)
        
        res = []
        
        for v in self.vertices:
            if va[1][v] == vb[1][v] and va[0][v] == vb[0][v] and va[0][v] != 0:
                res.append(v)
                
        return res
        
        
    def visited_bfs(self, v):
        timer = 0
        queue = []
        res = []
        
        visited = {}
        time = {}
        for i in self.vertices:
            visited[i] = 0
            time[i] = 0
        # print(visited)
        
        visited[v] = 1
        queue.append(v)
        print(queue)
        
        while len(queue) != 0:
            print(v, ":", queue)
            
            v = queue.pop(0)
            
            # print(self.vertices[v])
            
            timer+=1
            
            for n in self.vertices[v]:
                
                
                # print("n", n)
                # print(n, visited[n])
                if not visited[n]:
                    queue.append(n)
                    visited[n] =  1
                    time[n] = timer
                    res.append(n)
        
        print(res)    
        return visited, time
        
        
    def bfs(self, v):
        queue = []
        res = []
        
        visited = {}
        for i in self.vertices:
            visited[i] = 0
        print(visited)
        
        visited[v] = 1
        queue.append(v)
        print(queue)
        
        while len(queue) != 0:
            print(queue)
            
            v = queue.pop(0)
            
            
            
            print(self.vertices[v])
            
            
            for n in self.vertices[v]:
                print("n", n)
                print(n, visited[n])
                if not visited[n]:
                    queue.append(n)
                    visited[n] =  1
                    res.append(n)
            
        return res
        
    
            
            
v = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
e = [('A', 'E'), ('A', 'F'), ('B', 'A'), ('B', 'C'), ('C', 'D'),('C', 'G'), 
     ('D', 'E'), ('E', 'K'), ('E', 'F'), ('F', 'J'), ('G', 'H'), ('G', 'K'),
     ('K', 'H'), ('K', 'J'), ('J', 'H'), ('I', 'H'), ('I', 'J')] 

graph = Graph()
graph.create_graph(v, e)
# graph.print_graph()
# print(graph.reachable_nodes('A'))
# print(graph.reachable_nodes('B'))
a1 = graph.rendezvous_nodes('A', 'G')
a2 = graph.rendezvous_nodes('B', 'H')
a3 = graph.rendezvous_nodes('C', 'K')
# a4 = graph.rendezvous_nodes('A', 'I')
print("ans :", a1, "ans :", a2, "ans :", a3)
