from MinHeap import MinHeap


class HeapSort:

    def __init__(self, arr):
        self.numVertices = len(arr)
        self.position_of_vertex = [i for i in range(self.numVertices)]
        self.value_at_position = arr
        self.vertex_at_position = [i for i in range(self.numVertices)]

    def getPosition(self, vertex):
        return self.position_of_vertex[vertex]

    def minimum(self):
        return self.vertex_at_position[0], self.value_at_position[0]

    def findParentPosition(self, position):
        if position == 0:
            return -1
        return int((position - 1) / 2)

    def getVertexAtPosition(self, position):
        return self.vertex_at_position[position]

    def findSmallestChildPosition(self, position):

        if (2 * position) + 1 <= len(self.value_at_position) - 1:
            childPositionLeft = (2 * position) + 1
            if childPositionLeft + 1 <= len(self.value_at_position) - 1:
                childPositionRight = childPositionLeft + 1
            else:
                childPositionRight = -1
            valLeft = self.value_at_position[childPositionLeft]
            valRight = self.value_at_position[childPositionRight]
            if valLeft <= valRight:
                return childPositionLeft
            else:
                return childPositionRight
        else:
            return -1

    def updatePosition(self, vertex, position):
        self.position_of_vertex[vertex] = position

    def getValue(self, vertex_name):
        return self.value_at_position[self.getPosition(vertex_name)]

    def swap(self, position1, position2):
        self.vertex_at_position[position1], self.vertex_at_position[position2] = self.vertex_at_position[position2], \
                                                                                 self.vertex_at_position[position1]
        self.value_at_position[position1], self.value_at_position[position2] = self.value_at_position[position2], \
                                                                               self.value_at_position[position1]
        self.updatePosition(self.vertex_at_position[position1], position1)
        self.updatePosition(self.vertex_at_position[position2], position2)

    def heapify(self,n, position):

        smallest = position  # Initialize smalles as root
        l = 2 * position + 1  # left = 2*i + 1
        r = 2 * position + 2  # right = 2*i + 2

        # If left child is smaller than root
        if l < n and self.value_at_position[l] < self.value_at_position[smallest]:
            smallest = l

        # If right child is smaller than
        # smallest so far
        if r < n and self.value_at_position[r] < self.value_at_position[smallest]:
            smallest = r

        # If smallest is not root
        if smallest != position:
            # (arr[i],
            #  arr[smallest]) = (arr[smallest],
            #                    arr[i])
            self.swap(position,smallest)

            # Recursively heapify the affected
            # sub-tree
            self.heapify(n, smallest)

    def heapSort(self):
        for i in range(int(len(self.value_at_position)//2) - 1, -1, -1):
            self.heapify(len(self.value_at_position), i)

        # One by one extract an element
        # from heap
        for i in range(len(self.value_at_position) - 1, -1, -1):
            # Move current root to end #
            # arr[0], arr[i] = arr[i], arr[0]
            self.swap(i, 0)
            # call max heapify on the reduced heap
            self.heapify(i, 0)
        return self.value_at_position, self.vertex_at_position

