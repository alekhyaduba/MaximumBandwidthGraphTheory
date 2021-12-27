import random
# import seaborn as sn
# import pandas as pd
# import matplotlib.pyplot as plt


class Graph:

    def __init__(self, numOfVertices, edgeConnectivity, maxEdgeWeights):


        self.adjMatrix = [[0 for i in range(numOfVertices)] for j in range(numOfVertices)]
        self.maxEdgeWeight = maxEdgeWeights
        self.numVertices = numOfVertices
        self.edgeConnectivity = edgeConnectivity
        self.vertexDegree = [0 for i in range(numOfVertices)]
        self.numEdges = numOfVertices * edgeConnectivity / 2
        self.adjList = [[] for i in range(numOfVertices)]

        self.createGraph()

    #
    # def addVertices(self):
    #     """
    #     Adds the given number of vertices to the graph
    #     :param numberOfVertices: number of vertices to be added to the graph
    #     :return: none
    #     """
    #
    #     for i in range(self.numVertices):
    #         self.adjList[i] = []

    def addEdge(self, vertex1, vertex2):
        """
        Adds an undirected edge between two vertices
        :param vertex1: Vertex 1
        :param vertex2: Vertex 2
        :return: None
        """
        if self.adjMatrix[vertex1][vertex2] == 0:
            self.numEdges -= 1
            self.adjList[vertex1].append(vertex2)
            self.adjList[vertex2].append(vertex1)
            weight = random.randint(1, self.maxEdgeWeight)
            self.adjMatrix[vertex1][vertex2] = weight
            self.adjMatrix[vertex2][vertex1] = weight
            self.vertexDegree[vertex1] += 1
            self.vertexDegree[vertex2] += 1
            return True
        return False

    def printGraph(self):
        """
        Prints all the vertices and edges in the graph
        :return:
        """
        str_list = ""
        for index, val in enumerate(self.adjList):
            str_list += f"\n{index} : {val}"
        with open("graph.txt", "w") as fh:
            fh.write(str_list)
        # print(self.adjList)

    # def plot_graph(self):
    #     # array = [[33, 2, 0, 0, 0, 0, 0, 0, 0, 1, 3],
    #     #          [3, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     #          [0, 4, 41, 0, 0, 0, 0, 0, 0, 0, 1],
    #     #          [0, 1, 0, 30, 0, 6, 0, 0, 0, 0, 1],
    #     #          [0, 0, 0, 0, 38, 10, 0, 0, 0, 0, 0],
    #     #          [0, 0, 0, 3, 1, 39, 0, 0, 0, 0, 4],
    #     #          [0, 2, 2, 0, 4, 1, 31, 0, 0, 0, 2],
    #     #          [0, 1, 0, 0, 0, 0, 0, 36, 0, 2, 0],
    #     #          [0, 0, 0, 0, 0, 0, 1, 5, 37, 5, 1],
    #     #          [3, 0, 0, 0, 0, 0, 0, 0, 0, 39, 0],
    #     #          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    #     df_cm = pd.DataFrame(self.adjMatrix, index=[i for i in range(self.numVertices)],
    #                          columns=[i for i in range(self.numVertices)])
    #     plt.figure(figsize=(10, 10))
    #     sn.heatmap(df_cm, annot=True, cmap="OrRd")
    #     plt.savefig("plt_red.png", dpi=300)
    #     plt.show()

    def calculateAvgInDegree(self):
        """
        prints the average in degree of the vertices
        :return:
        """
        # print(self.numEdges * 2 / len(self.adjList))

    def createGraph(self):
        """
        Creates a graph pf given number of vertices and with given density/edge connectivity
        :param numVertices: Number of vertices in the graph
        :param edgeConnectivity: density of edges
        :return: graph
        """
        # Start the timer
        # start = timeit.default_timer()

        # Add vertices to the graph
        # self.addVertices()

        # Construct edges between two vertices according to the given edge density
        availableVertices = [i for i in range(0, self.numVertices)]

        # This loop ensures that the entire graph is connected
        for i in range(0, self.numVertices - 1):
            self.addEdge(i, i + 1)
        self.addEdge(self.numVertices - 1, 0)

        while self.numEdges > 0:
            # print(graph.numEdges, len(availableVertices))
            vertex1 = random.choice(availableVertices)
            vertex2 = random.choice(availableVertices)
            if vertex2 != vertex1:
                if self.addEdge(vertex1, vertex2):
                    if self.vertexDegree[vertex1] >= 1.05 * self.edgeConnectivity:
                        availableVertices.remove(vertex1)
                    if self.vertexDegree[vertex2] >= 1.05 * self.edgeConnectivity:
                        availableVertices.remove(vertex2)

        self.calculateAvgInDegree()
        # end = timeit.default_timer()
        # print((end - start))

    def getNumEdges(self):
        numEdges = 0

        for vList in self.adjList:
            for vertex in vList:
                numEdges += 1

        numEdges = int(numEdges/2)
        return numEdges

    def getEdgesListB(self):
        """
        This assumes that no self edges exists
        :return: A list with edge names as the index and [weight of edge , (u,v)]
        """
        edges_values_vertices = [[] for i in range(self.maxEdgeWeight + 1)]
        # edge_vertices = []
        for i in range(0,self.numVertices):
            for j in range(i+1, self.numVertices):
                if self.adjMatrix[i][j] != 0:
                    # edges.append([self.adjMatrix[i][j], (i, j)])
                    edges_values_vertices[self.adjMatrix[i][j]].append((i,j))
                    # edges_values_vertices.append(self.adjMatrix[i][j])
        return edges_values_vertices


    def getEdgesList(self):
        """
        This assumes that no self edges exists
        :return: A list with edge names as the index and [weight of edge , (u,v)]
        """
        edges_values = []
        edge_vertices = []
        for i in range(0,self.numVertices):
            for j in range(i+1, self.numVertices):
                if self.adjMatrix[i][j] != 0:
                    edge_vertices.append((i, j))
                    edges_values.append(self.adjMatrix[i][j])
        return edges_values, edge_vertices

