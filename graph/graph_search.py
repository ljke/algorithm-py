from collections import deque

from typing import List


class Graph:
    """
    undirected graph
    """

    def __init__(self, num_vertices):
        self._num_vertices = num_vertices
        self._adjacency = [[] for _ in range(num_vertices)]  # type: List[List[int]]

    def add_edge(self, s, t):  # type: (int, int) -> None
        """
        add each edge two times
        :param s:
        :param t:
        """
        self._adjacency[s].append(t)
        self._adjacency[t].append(s)

    def _generate_path(self, s, t, prev):
        """
        recursive call to print a path
        :param s: start vertex
        :param t: end vertex
        :param prev: prev list that store path info
        """
        if s != t:
            for path in self._generate_path(s, prev[t], prev):
                yield path
        yield str(t)

    def bfs(self, s, t):
        """
        use bfs to find path
        :param s: start vertex
        :param t: end vertex
        :return:
        """
        if s == t:
            return
        visited = [False] * self._num_vertices
        visited[s] = True
        q = deque()
        q.append(s)
        prev = [None] * self._num_vertices
        while q:
            v = q.popleft()
            # add neighbour of v
            for neighbour in self._adjacency[v]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    prev[neighbour] = v
                    if neighbour == t:
                        print "->".join(self._generate_path(s, t, prev))
                        return
                    else:
                        q.append(neighbour)

    def dfs(self, s, t):
        # because python2 not support nonlocal keyword, so use dict to store data
        # Inner functions are not prohibited from mutating the objects that Nonlocal variables refer to.
        flag = {"found": False}
        visited = [False] * self._num_vertices
        prev = [None] * self._num_vertices

        def _dfs(from_vertex):
            if flag["found"]:
                return
            visited[from_vertex] = True
            if from_vertex == t:
                flag["found"] = True
                return
            for neighbour in self._adjacency[from_vertex]:
                if flag["found"]:
                    return
                if not visited[neighbour]:
                    prev[neighbour] = from_vertex
                    _dfs(neighbour)

        _dfs(s)
        print "->".join(self._generate_path(s, t, prev))


if __name__ == "__main__":
    graph = Graph(8)

    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 7)
    graph.add_edge(6, 7)

    graph.bfs(0, 7)
    graph.dfs(0, 7)
