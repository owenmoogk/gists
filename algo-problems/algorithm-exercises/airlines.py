class Graph:

    def __init__(self, edges):
        self.edges = edges
        self.graphDict = {}
        for start, end in self.edges:
            if start in self.graphDict:
                self.graphDict[start].append(end)
            else:
                self.graphDict[start] = [end]

    def getPaths(self, start, end, path=[]):
        
        path = path + [start] # path holds the current path

        if start == end: # break case
            return [path]

        if start not in self.graphDict: # if there are no outgoing flights
            return []

        paths = [] # paths holds all possible paths
        for node in self.graphDict[start]:
            if node not in path: # prevents circular loops
                new_paths = self.getPaths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return(paths)

    def getShortestPath(self, start, end, path = []):
        path = path + [start]
        if start == end:
            return(path)
        if start not in self.graphDict:
            return(None)
        
        shortestPath = None
        for node in self.graphDict[start]:
            if node not in path: # prevents circular loops
                newpath = self.getShortestPath(node, end, path)
                if sp:
                    if shortestPath is None or len(newpath) < len(shortestPath):
                        shortestPath = sp
        return(shortestPath)


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
        ("Paris", "Mumbai") # circular tester :)
    ]

    routeGraph = Graph(routes)
    print(routeGraph.getShortestPath("Mumbai","New York"))