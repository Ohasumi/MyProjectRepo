"""
    Author: Thanakit Yuenyongphisit
    Date  : 03/04/2022
    Purpose: for CS365 HomeWork ID 6309682000
    DepthFirstSearch algorithms in python
"""
# for mark visited
class DepthFirstSearch:
    def __init__(self):
        self.visited = []
        self.limited = 30
        self.graph = dict()

    def addEdge(self, u: str, v: str):
        # when node first assigned must create list
        if u not in self.graph:
            self.graph[u] = []
        # None input
        if v is None:
            return

        self.graph[u].append(v)

    def addEdgeList(self, u: str, v: list):  # v = None if no edge
        # If vertex not add already
        if u not in self.graph:
            self.graph[u] = []
        # empty list or None will only create vertex
        if v is None or (isinstance(v, list) and len(v) == 0):
            return

        # if correct type then add to graph
        elif isinstance(v, list):  # ('A', ['B', 'C'])
            self.graph[u].extend(v)

    def dfs(self, visited: list, node: str, goal: str) -> object:
        # visited
        # when founded goal return this node
        if node == goal:
            return [goal]

        # check limited expand

        if (self.limited <= 0):
            return None
        # mark vistited
        visited.append(node)

        # expanded node
        self.graph[node].sort()  # for alway expand a->z

        self.limited = self.limited - 1

        for child in self.graph[node]:
            # encounter visited node will ignore
            if child in visited:
                continue
            result = self.dfs(visited, child, goal)
            # cutoff due to limit expanded
            if result is None:
                return None
            # when found solution this node extended result
            if len(result) > 0:
                tmp = [node]
                tmp.extend(result)
                return tmp
        return []

    def search(self, start, goal):
        result = self.dfs([], start, goal)
        self.visited = []#reset visited
        if result is None or len(result) == 0:
            print("No solution!")
            return
        for each in result:
            if each != start:
                print(" -> ", end="")
            print(each, end="")


def main():
    g = DepthFirstSearch()
    g.addEdgeList("A", ['G', 'C'])
    g.addEdgeList("B", ['A', 'D'])
    g.addEdgeList("C", ['B', 'H'])
    g.addEdgeList("D", ['E', 'F'])
    g.addEdgeList("E", ['F'])
    g.addEdgeList("F", [])
    g.addEdgeList("G", ['D', 'E'])
    g.addEdgeList("H", ['A', 'D'])
    g.addEdgeList("S", ['A', 'B', 'C'])
    g.search('S', 'F')


main()
