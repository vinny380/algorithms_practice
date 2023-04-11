import random
from queue_1 import Queue

class Vertex:
    def __init__(self, key):
        self.key = key
        self.edges = []

    def add_edge(self, v, weight):
        self.weight = weight
        self.edges.append((v, weight))

    def __getitem__(self, item):
         return self.edges[item]        


class Graph:
    def __init__(self, num_vertices):
        self.vertices = []
        self.num_vertices = num_vertices
        for i in range(1, num_vertices + 1):
            new_vertex = Vertex(i)
            self.vertices.append(new_vertex)
            for j in range(1, i):
                if random.random() < 0.5:
                    weight = random.randint(10, 100)
                    self.vertices[i-1].add_edge(j, weight)
                    self.vertices[j-1].add_edge(i, weight)

    def add_vertex(self):
        last_vertex = self.vertices[-1].key
        new_vertex_key = last_vertex + 1
        new_vertex = Vertex(new_vertex_key)
        self.vertices.append(new_vertex)
        for v in self.vertices[:-1]:
            if random.random() < 0.6:
                weight = random.randint(10, 100)
                v.add_edge(new_vertex_key, weight)
                new_vertex.add_edge(v.key, weight)
        return new_vertex


    def bfs(self, start_vertex=0):
        visited = [False for n in self.vertices]
        queue = Queue()
        queue.enqueue(start_vertex)                
        visited[start_vertex] = True
        bfs_tree = Graph(self.num_vertices)
            
        while not queue.is_empty():
            v = queue.dequeue()
            for neighbor in self.vertices[v].edges:
                if not visited[neighbor[0]-1]:
                    queue.enqueue(neighbor[0]-1)
                    visited[neighbor[0]-1] = True
                    bfs_tree.vertices[v].add_edge(bfs_tree.vertices[neighbor[0]-1], 3)
        return bfs_tree

    def prim(self):
        visited = [False] * self.num_vertices
        min_edge = [float('inf')] * self.num_vertices
        parent = [None] * self.num_vertices

        # Start from vertex 0
        min_edge[0] = 0
        parent[0] = -1
        for i in range(self.num_vertices):
            # Find the unvisited vertex with the smallest minimum edge
            min_vertex = None
            for j in range(self.num_vertices):
                if not visited[j] and (min_vertex is None or min_edge[j] < min_edge[min_vertex]):
                    min_vertex = j

            # Mark the vertex as visited
            visited[min_vertex] = True

            # Update the minimum edge and parent for each unvisited neighbor
            for neighbor, weight in self.vertices[min_vertex].edges:
                if not visited[neighbor-1] and weight < min_edge[neighbor-1]:
                    min_edge[neighbor-1] = weight
                    parent[neighbor-1] = min_vertex

        # Build the minimum spanning tree
        mst = Graph(self.num_vertices)
        for i in range(1, self.num_vertices):
            mst.vertices[parent[i]].add_edge(mst.vertices[i], min_edge[i])

        return mst

    def mst_weight(self):
        mst_weight = []
        for i in self.vertices:
            mst_weight.append(i[0][0])
        return sum(mst_weight)

    def experiment(self, k=5):
        n_values = [20, 40, 60]
        k = k
        
        for n in n_values:
            diff_total = 0
            for i in range(k):
                # Generate random graph
                graph = Graph(n)
                
                # Find minimum spanning tree using BFS
                bfs_tree = graph.bfs()
                bfs_weight = bfs_tree.mst_weight()
                
                # Find minimum spanning tree using Prim's algorithm
                prim_tree = graph.prim()
                prim_weight = prim_tree.mst_weight()
                
                # Compute difference between BFS and Prim's MST weights
                diff = ((bfs_weight - prim_weight) / prim_weight) * 100
                diff_total += diff
                
            # Compute average difference
            avg_diff = diff_total / k
            
            # return results
            return f"Average difference for n={n}: {avg_diff}%"        

if __name__ == '__main__':
    
#     # for v in g.vertices:
#         # print('\n',v.key, '->', v.edges,'\n', '\n')

#     # use BFS to find a spanning tree and its weight
#     # bfs_tree = g.bfs()
#     # for v in bfs_tree.vertices:
#     #         print('\n',v.key, '->', v.edges,'\n', '\n')   
#     mst = g.prim() 
#     for v in mst.vertices:
#         print('\n',v.key, '->', v.edges,'\n', '\n')       
#     # bfs_weight = sum([edge[2] for edge in bfs_tree])
#     # print(bfs_tree)

