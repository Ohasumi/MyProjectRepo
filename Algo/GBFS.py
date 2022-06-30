"""
    Author: Thanakit Yuenyongphisit
    Date  : 03/04/2022
    Purpose: for CS365 HomeWork ID 6309682000

"""
from queue import PriorityQueue


class GreedyBestFirstSearch:

    def __init__(self):
        self.graph = dict()

        self.h = dict()  # heuristic
        self.reachby = dict()
        self.limited = 30

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

    def addHeuristic(self, u: str, v: int):
        self.h[u] = v

    def resetHeuristic(self):
        self.h = dict()

    def solution(self, start, goal):
        result = []
        node = goal
        result.append(node)
        while node != start:
            node = self.reachby[node]
            result.append(node)
        return result[::-1]

    def search(self, start, goal):
        if (self.GBFSUtility(start, goal)):
            for each in self.solution(start, goal):
                if each != start:
                    print(" -> ", end="")
                print(each, end="")
        else:
            print("No solution")

    def GBFSUtility(self, start, goal):
        pq = PriorityQueue()
        pq.put((self.h[start], start))  # value, node
        visited = set()

        # loop till priorityqueue empty
        while not pq.empty():
            node = pq.get()[1]
            # check goal
            if self.h[node] == 0 or node == goal:
                return True

            # limit check
            if self.limited <= 0:
                return False
            self.limited -= 1

            for child in self.graph[node]:
                if child not in visited:
                    # Keep tracking for solution
                    self.reachby[child] = node

                    # visited when found then add to priority queue
                    visited.add(child)
                    pq.put((self.h[child], child))
        return False


def main():
    g = GreedyBestFirstSearch()
    g.addEdgeList("A", ['G', 'C'])
    g.addEdgeList("B", ['A', 'D'])
    g.addEdgeList("C", ['B', 'H'])
    g.addEdgeList("D", ['E', 'F'])
    g.addEdgeList("E", ['F'])
    g.addEdgeList("F", [])
    g.addEdgeList("G", ['D', 'E'])
    g.addEdgeList("H", ['A', 'D'])
    g.addEdgeList("S", ['A', 'B', 'C'])

    g.addHeuristic('A', 8)
    g.addHeuristic('B', 9)
    g.addHeuristic('C', 7)
    g.addHeuristic('D', 4)
    g.addHeuristic('E', 3)
    g.addHeuristic('F', 0)
    g.addHeuristic('G', 6)
    g.addHeuristic('H', 6)
    g.addHeuristic('S', 10)

    g.search('S', 'F')

main()
