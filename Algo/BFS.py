"""
    Author: Thanakit Yuenyongphisit
    Date  : 03/04/2022
    Purpose: for CS365 HomeWork ID 6309682000

"""
# for mark explored
class BreadFirstSearch:

    def __init__(self):
        self.limited = 30
        self.previous = dict()
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



    def solution(self, start, goal):
        result = []
        now = goal
        while True:
            # trace back to start node
            result.append(now)
            if now == start:
                return result[::-1]
            # go back 1 step
            now = self.previous[now]


    def BFSUtility(self, node, goal):
        # add node to queue

        explored = set()
        queue = []
        queue.append(node)

        # Check goal
        if node == goal:
            return [node]
        count = 0
        # loop
        while len(queue) != 0:
            now = queue.pop(0)
            explored.add(now)
            count += 1
            # check limited
            if count > 30:
                return False

            self.graph[now].sort()
            for child in self.graph[now]:
                # check explored
                # add to frontier
                if child not in explored and child not in queue:
                    # mark reached by
                    self.previous[child] = now
                    if child == goal:
                        return True
                    queue.append(child)
        # failure
        return None


    def search(self, start, goal):
        if (self.BFSUtility(start, goal)):
            for each in self.solution(start, goal):
                if each != start:
                    print(" -> ", end="")
                print(each, end="")
        else:
            print("No solution")
        #reset
        self.limited = 30
        self.previous = dict()


def main():
    g = BreadFirstSearch()
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
