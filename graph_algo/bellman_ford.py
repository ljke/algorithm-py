# coding=utf-8

# Bellman-Ford算法，计算单源图最短路径


class Graph(object):
    def __init__(self, vertices):
        super(Graph, self).__init__()
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])

    def bellman_ford(self, src):
        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("Inf")] * self.V
        prev = [0] * self.V
        dist[src] = 0

        # Step 2: Relax all edge |V|-1 times.
        # A simple shortest path from src to any other vertex can have at-most |V|-1 edges
        for i in range(self.V - 1):
            for u, v, w in self.edges:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u

        # Step 3: check for negative-weight cycles, the above step
        # guarantees shortest distances if graph doesn't contain negative weight cycle
        for u, v, w in self.edges:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                return
        return dist, prev


def print_arr(hint_str, arr):
    print hint_str
    for i in range(len(arr)):
        print "%d \t\t %d" % (i, arr[i])


if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    rst_dist, rst_prev = g.bellman_ford(0)

    print_arr("Vertex   Distance from Source", rst_dist)
    print_arr("Vertex   predecessor", rst_prev)