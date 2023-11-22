class Node():
    def __init__(self, value):
        self.parent = None
        self.value = value
        self.children = []
        
class Tree():
    def __init__(self, root_val):
        self.root = Node(root_val)
        self.nodes = {}
        self.nnodes = {}
        
    def create_tree(self, edges):
        self.nodes[self.root.value] = self.root
        for edge in edges:
            vertex_1 = Node(edge[1])
            if edge[0] not in self.nodes:
                self.nodes[edge[0]] = Node(edge[0])
            self.nodes[edge[0]].children.append(vertex_1)
            if edge[1] not in self.nodes:
                self.nodes[edge[1]] = vertex_1
                
    def print_tree(self):
        print(self.nodes)
        for _, node in self.nodes.items():
            for child in node.children:
                print(f"Node : {node.value}, Children : {child.value}")

    def bfs(self):
        queue = []
        visited = {}
        leaf = []
        all_nodes = []
        
        queue.append(self.root)
        visited[self.root.value] = True
          
        while len(queue) != 0:
            v = queue.pop(0)
            visited[v.value] = 1
            for child in v.children:
                if not visited[child.value]:    
                    queue.append(child)
            all_nodes.append(v)     
            if len(v.children) == 0:
                leaf.append(v)
            
        return all_nodes, leaf
    
    def remove(self, leaf):
        for l in leaf:
            del self.nodes[l.value]
        self.nnodes = self.nodes

number_of_nodes = int(input())
root_val = input()
tree = Tree(root_val=root_val)

number_of_edges = int(input())
edge_list = []
for i in range(number_of_edges):
    s = input()
    edge = s.strip().split()
    edge_list.append(edge)

tree.create_tree(edge_list) 
tree.print_tree()           

all_nodes, leaf = tree.bfs()
print(",".join([a.value for a in leaf]))

tree.remove(leaf)
leaf_new = tree.bfs()
print(",".join([a.value for a in leaf_new]))
