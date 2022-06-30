"""
    Author: Thanakit Yuenyongphisit
    Date  : 03/04/2022
    Purpose: for CS365 HomeWork ID 6309682000

"""


# Class creation
class BreadFirstSearch:

    def __init__(self):
        self.limited = 30  # for limited explanding in each node
        self.previous = dict()  # key for present node, value for previous using for trace back
        self.graph = dict()  # key for present node, value is list of connected node

    # for adding individual node
    def addEdge(self, u: str, v: str):
        # when node first assigned must create list
        if u not in self.graph:
            self.graph[u] = []
        # Case adding node isn't have an edge
        if v is None:
            return

        # adding connected node to this node
        self.graph[u].append(v)

    # for add list of node
    def addEdgeList(self, u: str, v: list):  # v = None if no edge
        # create node if node isn't existed.
        if u not in self.graph:
            self.graph[u] = []

        # empty list or None will only create vertex so return
        if v is None or (isinstance(v, list) and len(v) == 0):
            return

        # correctly format will add all input node to existing node
        elif isinstance(v, list):  # ('A', ['B', 'C'])
            for each in v:
                if each not in self.graph[u]:
                    self.graph[u].append(each)
    #using to generate path in the correct direction in case search are success
    #helper function use in search
    def solution(self, start, goal):
        result = []
        now = goal
        while True:
            # trace back to start node
            result.append(now)

            if now == start:
                return result[::-1] #according to result list are in reversed direction

            # go back 1 step ( this is backward pathing)
            now = self.previous[now]

    # Helper function using in search to determine succesfulness
    def BFSUtility(self, node, goal):
        # add node to queue

        explored = set()
        queue = [node] #add first node to queue

        # Check goal
        if node == goal:
            return True
        count = 0
        # loop
        while len(queue) != 0:
            now = queue.pop(0)  # get value from queue
            explored.add(now)  # marked present node as explored
            # check limited
            count += 1  # limited count
            if count > self.limited:
                return False

            self.graph[now].sort()  # isn't neccessary (Just for expanding from alphabet sequence

            # literally visited each of child node from present node
            for child in self.graph[now]:
                # adding node to queue, mustn't explored nor queued (prevent redundant visited)
                if child not in explored and child not in queue:

                    self.previous[child] = now  # Saving path from previuos node
                    # in BFS node isn't need to explanded before checking goal
                    if child == goal:
                        return True
                    # if node isn't goal then add to queue
                    queue.append(child)
        # failure
        return None

    #Working function
    def search(self, start, goal):
        #Checking, is it success or fail?
        if self.BFSUtility(start, goal):
            #get path node from helper function
            for each in self.solution(start, goal):
                if each != start:
                    print(" -> ", end="")
                print(each, end="")
        else:
            print("No solution")
        # reset
        self.limited = 30
        self.previous = dict()

#example
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
