"""
    Author: Thanakit Yuenyongphisit
    Date  : 03/04/2022
    Purpose: for CS365 HomeWork ID 6309682000

"""
class UCF:
    # constructor
    def __init__(self):
        self.graph = dict()
        self.reachby = dict()
        self.limited = 30

    # add edge to graph
    def addEdge(self, u: str, v: str, w: int):
        # when node first assigned must create list
        if u not in self.graph:
            self.graph[u] = []
        # None input
        if v is None:
            return

        self.graph[u].append([v, w])

    def addEdgeList(self, u: str, v: list):# v = None if no edge
        #None input or empty list do nothing if already assined node
        #otherwise create vertex
        if v is None or (isinstance(v, list) and len(v) == 0):
            if u not in self.graph:
                self.graph[u] = []

        elif isinstance(v[0], list):  # ('A', [['B', 2], ['C', 3]])
            # when node first assigned must create list
            if u not in self.graph:
                self.graph[u] = []

            self.graph[u].extend(v)
        else:
            print("Wrong format: Eg. addEdgeList('A', [['B', 2], ['C', 3]]) ")

    def setGraph(self, g):
        self.graph = g

    def solution(self, start, goal):  # back trace to start node
        now = goal
        result = []
        result.append(now)
        while start != now:
            now = self.reachby[now]
            result.append(now)
        return result[::-1]

    def search(self, start, goal):
        if (self.utilityUFCS(start, goal)):
            for each in self.solution(start, goal):
                if (each != start):
                    print(" -> ", end="")
                print(each, end="")
        else:
            print("No solution")

    def utilityUFCS(self, start, goal):
        # independent variable for each run
        frontier = dict()  # dict {'Node': weight}
        explored = set()  # collect just node name not weight
        self.reachby = dict()  # use to get solution
        # empty dict = failure
        if not self.graph or start not in self.graph:
            return None
        # start node will be 0 path cost
        frontier[start] = 0

        # loop till frontier empty
        while frontier:
            # get minimum distance node from frontier
            #node = sorted(frontier.items(), key=lambda item: item[1]).pop(0)

            #case when equal weight
            arr = sorted(frontier.items(), key=lambda item: item[1])
            arr = [(k, v) for k, v in arr if v == arr[0][1]]
            node = sorted(arr, key=lambda item: item[0]).pop(0)
            #node = arr.pop(0)
            # remove node from frontier

            frontier.pop(node[0])
            #print(node, frontier)
            # Check goal
            if node[0] == goal:
                return True

            explored.add(node[0])  # mark as explored

            # limited expandation
            if self.limited <= 0:
                return False
            self.limited -= 1

            # each action of exploring node
            # case node isn't add properly to graph meaning this node no child and if it not goal also then ignored
            if node[0] not in self.graph:
                continue
            for child in self.graph[node[0]]:  # child = ['neibourgh node', weight]
                # add child to frontier
                # case not in frontier
                if child[0] not in explored and child[0] not in frontier:
                    self.reachby[child[0]] = node[0]
                    frontier[child[0]] = child[1] + node[1] # now weight + previous weight

                # case in frontier but found better path
                elif child[0] not in explored and child[0] in frontier:
                    if child[1]+node[1] < frontier[child[0]]:
                        self.reachby[child[0]] = node[0]
                        frontier[child[0]] = child[1]+node[1]

        return False


def main():
    g = UCF()
    g.addEdgeList("A", [['G', 2], ['C', 3]])
    g.addEdgeList("B", [['A', 5], ['D', 6]])
    g.addEdgeList("C", [['B', 4], ['H', 3]])
    g.addEdgeList("D", [['E', 2], ['F', 3]])
    g.addEdgeList("E", [['F', 5]])
    g.addEdgeList("F", [])
    g.addEdgeList("G", [['D', 4], ['E', 5]])
    g.addEdgeList("H", [['A', 4], ['D', 4]])
    g.addEdgeList("S", [['A', 3], ['B', 2]])

    g.search("S", "F")

main()
