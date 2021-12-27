from MaxHeapV1 import MaxHeap
from Graph import Graph
import timeit
from HeapSort import HeapSort
import yappi
import sys




def MaxBandwidthDijkstraNoHeap(graph, source, destination):
    """
    Gives out the maximum bandwidth path between source and destination.
    :param graph:
    :type graph: Graph
    :param source: source vertex
    :param destination: destination vertex
    :return:
    """

    def getFringeMaxBW(bw, fringes):
        """
        returns the fringe vertex with max bandwidth
        :param bw:
        :return:
        """
        vertex_with_max_bw = -1
        maximum = 0
        for vertex in fringes:
            if bw[vertex] >= maximum:
                vertex_with_max_bw = vertex
                maximum = bw[vertex]
        return vertex_with_max_bw


    # 1.
    fringes = []
    status = [-1 for i in range(graph.numVertices)]  # All vertices are marked as unseen
    dad = [0 for i in range(graph.numVertices)]
    bw = [0 for i in range(graph.numVertices)]

    # 2.
    status[source] = 1

    # 3.
    for w in graph.adjList[source]:
        status[w] = 0  # make fringe
        fringes.append(w)
        dad[w] = source
        bw[w] = graph.adjMatrix[source][w]

    # 4.
    while len(fringes) > 0:
        v = getFringeMaxBW(bw, fringes)
        status[v] = 1
        fringes.remove(v)

        for w in graph.adjList[v]:
            if status[w] == -1:
                status[w] = 0
                fringes.append(w)
                bw[w] = min(bw[v], graph.adjMatrix[v][w])
                dad[w] = v

            elif status[w] == 0 and bw[w] < min(bw[v], graph.adjMatrix[v][w]):
                bw[w] = min(bw[v], graph.adjMatrix[v][w])
                dad[w] = v

    # 5.

    if status[destination] != 1:
        return ([])
    else:
        mini = sys.maxsize
        result = []
        x = destination
        result.append(x)
        # if bw[x] < mini:
        #     mini = bw[w]
        while x != source:
            if graph.adjMatrix[x][dad[x]] < mini:
                mini = graph.adjMatrix[x][dad[x]]
            x = dad[x]
            result.append(x)

        print(f"Max BW: {mini}")
        return result


def MaxBandwidthDijkstraHeap(graph, source, destination):
    """

    :param graph:
    :type Graph
    :param source:
    :param destination:
    :return:
    """

    # 1.
    fringes = MaxHeap(graph.numVertices)
    status = [-1 for i in range(graph.numVertices)]  # All vertices are marked as unseen
    dad = [0 for i in range(graph.numVertices)]
    bw = [0 for i in range(graph.numVertices)]

    # 2.
    status[source] = 1

    # 3.
    for w in graph.adjList[source]:
        status[w] = 0  # make fringe
        # fringes.append(w)
        bw[w] = graph.adjMatrix[source][w]
        dad[w] = source
        # print(f"inserting {bw[w]}")
        fringes.insert(w, bw[w])
        # print(fringes.printHeap())

    # 4.
    while len(fringes) > 0:
        v, _ = fringes.maximum()
        status[v] = 1
        # print(f"deleting {fringes.value_at_position[fringes.position_of_vertex[v]]}")
        fringes.delete(v)
        # fringes.printHeap()

        for w in graph.adjList[v]:
            if status[w] == -1:
                status[w] = 0
                bw[w] = min(bw[v], graph.adjMatrix[v][w])
                dad[w] = v
                # print(f"inserting {v},{w}, {bw[w]}")
                fringes.insert(w, bw[w])
                # print(fringes.printHeap())

            elif status[w] == 0 and bw[w] < min(bw[v], graph.adjMatrix[v][w]):
                bw[w] = min(bw[v], graph.adjMatrix[v][w])
                dad[w] = v
                # print(f"bw update rule delete {v} {w}")
                # print(f"deleting {fringes.value_at_position[fringes.position_of_vertex[w]]}")
                fringes.delete(w)
                # fringes.printHeap()
                # print(f"inserting {bw[w]}")
                fringes.insert(w, bw[w])

    # 5.

    if status[destination] != 1:
        return ([])
    else:
        mini = sys.maxsize
        result = []
        x = destination
        result.append(x)
        # if bw[x] < mini:
        #     mini = bw[w]
        while x != source:
            if graph.adjMatrix[x][dad[x]] < mini:
                mini = graph.adjMatrix[x][dad[x]]
            x = dad[x]
            result.append(x)

        print(f"Max BW: {mini}")
        return result



def maxBandwidthKruskals(graph, source, destination):
    """

    :param graph:
    :type Graph
    :param source:
    :param destination:
    :return:
    """
    parentArray = []
    heightArray = []
    def find(vertex):
        w = vertex
        while parentArray[w] != -1:
            w = parentArray[w]
        return w

    def makeSet(graph):
        """

        :param graph:
        :type Graph
        :return:
        """
        for i in range(graph.numVertices):
            parentArray.append(-1)
            heightArray.append(0)

    def union(r1, r2):
        if heightArray[r1] > heightArray[r2]:
            parentArray[r2] = r1
        elif heightArray[r2] > heightArray[r1]:
            parentArray[r1] = r2
        else:
            parentArray[r2] = r1
            heightArray[r1] += 1

    # def sortEdgesB(graph):
    #     start = timeit.default_timer()
    #     sorted_edges = []
    #     edges_value_vertices = graph.getEdgesListB()
    #     for x in range(len(edges_value_vertices) - 1, -1, -1):
    #         for ver_pair in edges_value_vertices[x]:
    #             sorted_edges.append(ver_pair)
    #     end = timeit.default_timer()
    #     # print(f"time for sorting {end-start}")
    #     return sorted_edges

    def sortEdges(graph):
        start = timeit.default_timer()
        sorted_edges = []
        edges_values, edges_vertices = graph.getEdgesList()
        edges = HeapSort(edges_values)
        edges_value_sorted, edges_index = edges.heapSort()
        for i in range(len(edges_index)):
            sorted_edges.append(edges_vertices[edges_index[i]])

        end = timeit.default_timer()
        # print(f"time taken for sort: {end - start}")
        return sorted_edges
        # edges_values = []
        # edges_vertices = []
        # name_index = 0
        # for i in range(0, graph.numVertices):
        #     for j in range(i + 1, graph.numVertices):
        #         if graph.adjMatrix[i][j] != 0:
        #             # edges.append([self.adjMatrix[i][j], (i, j)])
        #             edges_vertices.append((i, j))
        #             edges_values.append(graph.adjMatrix[i][j])
        #             edge_heap.insert(name_index, graph.adjMatrix[i][j])
        #             name_index += 1
        # end = timeit.default_timer()
        # print(f"heap creation time {end - start}")

        # for name, edge_value in enumerate(edges_values):
        #     edge_heap.insert(name, edge_value)
        #
        # for i in range(len(edges_values)):
        #     edge_heap.insert(i, edges_values[i])

        # start = timeit.default_timer()
        # while len(edge_heap) > 0:
        #     popped_edge_name, popped_weight = edge_heap.popMax()
        #     sorted_edges.append(edges_vertices[popped_edge_name])
        #     # print(f"popping {popped_weight}")
        # end = timeit.default_timer()
        # print(f"sorting time {end- start}")
        # return sorted_edges

    def maxSpanningTree(graph):
        """

        :param graph:
        :type Graph
        :return:
        """
        spanningTree = [[] for i in range(graph.numVertices)]
        sorted_edges = sortEdges(graph)
        makeSet(graph)
        for i in range(len(sorted_edges)):
            u, v = sorted_edges[i]
            r1 = find(u)
            r2 = find(v)
            if r1 != r2:
                union(r1, r2)
                spanningTree[u].append(v)
                spanningTree[v].append(u)

        return spanningTree

    def buildPath(max_spanning_tree, source, destination, graph):
        # bfs
        # O(n)
        # 0 - > white, 1- gray, -1->black
        path = []
        parent = [-1 for i in range(len(max_spanning_tree))]
        q = []
        color = [0 for i in range(len(max_spanning_tree))]
        q.append(source)
        color[source] = -1
        while len(q) > 0:
            v = q.pop()
            for w in max_spanning_tree[v]:
                if color[w] == 0:
                    q.append(w)
                    parent[w] = v
                    color[w] = -1

        x = destination
        path.append(x)
        mini = sys.maxsize
        while x != source:
            weight = graph.adjMatrix[x][parent[x]]
            if weight < mini:
                mini = weight
            x = parent[x]
            path.append(x)
        print(f"Max BW : {mini}")
        return path

    start = timeit.default_timer()
    max_spanning_tree = maxSpanningTree(graph)
    end = timeit.default_timer()
    # print(f"time taken to build spanning tree {end - start}")
    # print(max_spanning_tree)
    start = timeit.default_timer()
    path = buildPath(max_spanning_tree, source, destination,graph)
    end = timeit.default_timer()
    # print(f"time taken for path building {end - start}")
    return path

def main():
    source = 3
    destination = 1887
    start = timeit.default_timer()
    sparse_graph = Graph(5000, 1000, 1000)
    end = timeit.default_timer()
    print(f"Time to build the graph: {end - start}s")
    # dense_graph = Graph(5000, 1000, 1000)
    start = timeit.default_timer()
    path = MaxBandwidthDijkstraNoHeap(sparse_graph, source, destination)
    end = timeit.default_timer()
    time = end - start
    print(f"Time taken for Djikstra without heap: {time}s")
    start = timeit.default_timer()
    path_1 = MaxBandwidthDijkstraHeap(sparse_graph, source, destination)
    end = timeit.default_timer()
    print(f"Time taken Djikstra with heap: {(end - start)}s")
    # yappi.set_clock_type("cpu")  # Use set_clock_type("wall") for wall time
    # yappi.start()
    start = timeit.default_timer()
    path_k = maxBandwidthKruskals(sparse_graph, source, destination)
    end = timeit.default_timer()
    print(f"Time taken kruskals: {end - start}s")
    # yappi.get_func_stats().print_all()
    # yappi.get_thread_stats().print_all()

    print(f"heap path: {path_1}")
    print(f"no heap path: {path}")
    print(f"kruskals path: {path_k}")



    # print(sparse_graph.adjMatrix)

if __name__ == "__main__":
    main()


