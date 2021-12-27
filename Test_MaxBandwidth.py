from MaxBandwidth import MaxBandwidthDijkstraNoHeap
from MaxBandwidth import MaxBandwidthDijkstraHeap
from MaxBandwidth import maxBandwidthKruskals
from Graph import Graph
import random
from timeit import default_timer as timer


def main():
    for i in range(1, 6):
        graph = Graph(5000, 6, 1000)
        for j in range(1, 6):
            source = random.randint(0, graph.numVertices - 1)
            destination = random.randint(0, graph.numVertices - 1)
            print(f"Sparse Graph G1:{i} Case{j}: source: {source} destination: {destination}")

            print(f"Dijkstra without Heap:")
            start = timer()
            path_mb = MaxBandwidthDijkstraNoHeap(graph, source, destination)
            end = timer()
            print(f"Time taken : {end - start}")

            print(f"Dijkstra with Heap:")
            start = timer()
            path_mb_heap = MaxBandwidthDijkstraHeap(graph, source, destination)
            end = timer()
            print(f"Time taken : {end - start}")

            print(f"Kruskals with heapsort")
            start = timer()
            path_kruskals = maxBandwidthKruskals(graph, source, destination)
            end = timer()
            print(f"Time taken : {end - start}")
    for i in range(1, 6):
        graph = Graph(5000, 1000, 1000)
        for j in range(1, 6):
            source = random.randint(0, graph.numVertices - 1)
            destination = random.randint(0, graph.numVertices - 1)
            print(f"Dense Graph G2:{i} Case{j}: source: {source} destination: {destination}")

            print(f"Dijkstra without Heap:")
            start = timer()
            path_mb = MaxBandwidthDijkstraNoHeap(graph, source, destination)
            end = timer()
            print(f"Time taken : {end - start}")

            print(f"Dijkstra with Heap:")
            start = timer()
            path_mb_heap = MaxBandwidthDijkstraHeap(graph, source, destination)
            end = timer()
            print(f"Time taken : {end - start}")

            print(f"Kruskals with heapsort")
            start = timer()
            path_kruskals = maxBandwidthKruskals(graph, source, destination)
            end = timer()
            print(f"Time taken : {end - start}")

if __name__ == "__main__":
    main()
