import sys

from Graph import Graph
from MaxHeapV1 import MaxHeap
import timeit
import yappi

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


def MaxBandwidthDijkstraNoHeap(graph, source, destination):
    """
    Gives out the maximum bandwidth path between source and destination.
    :param graph:
    :type graph: Graph
    :param source: source vertex
    :param destination: destination vertex
    :return:
    """
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
        if bw[x] < mini:
            mini = bw[w]
        while x != source:
            x = dad[x]
            result.append(x)
            if bw[x] < mini:
                mini = bw[w]
        print(f" no heap mini {mini}")
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
        if bw[x] < mini:
            mini = bw[w]
        while x != source:
            x = dad[x]
            result.append(x)
            if bw[x] < mini:
                mini = bw[w]
        print(f" heap mini {mini}")
        return result


def MaxBandwidthKruskals(graph, source, destination):
    """

    :param graph:
    :type Graph
    :param source:
    :param destination:
    :return: 
    """

    pass


def main():
    start = timeit.default_timer()
    sparse_graph = Graph(5000, 1000, 1000)
    end = timeit.default_timer()
    print(f"time to build the graph: {end - start}")
    # dense_graph = Graph(5000, 1000, 1000)
    start = timeit.default_timer()
    path = MaxBandwidthDijkstraNoHeap(sparse_graph, 499, 10)
    end = timeit.default_timer()
    time = end - start
    print(f"no heap time taken {time}")

    # for i in range(sparse_graph.numVertices):
    #     for j in range(sparse_graph.numVertices):
    #         if sparse_graph.adjMatrix[i][j] != 0:
    #             print(f"{i}, {j}-> {sparse_graph.adjMatrix[i][j]}")
    # # print(sparse_graph.adjMatrix)

    # yappi.set_clock_type("cpu")  # Use set_clock_type("wall") for wall time
    # yappi.start()
    start = timeit.default_timer()
    path_1 = MaxBandwidthDijkstraHeap(sparse_graph, 499, 10)
    end = timeit.default_timer()
    print(f"heap time {(end - start)}")

    print(f"heap path: {path_1}")
    print(f"no heap path: {path}")
    # yappi.get_func_stats().print_all()
    # yappi.get_thread_stats().print_all()

if __name__ == "__main__":
    main()
