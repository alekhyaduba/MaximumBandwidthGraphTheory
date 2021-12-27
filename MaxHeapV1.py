import math


class MaxHeap:

    def __init__(self, numOfVertices):
        self.numVertices = numOfVertices
        self.position_of_vertex = [-1 for i in range(numOfVertices)]
        self.value_at_position = []
        self.vertex_at_position = []


    def __len__(self):
        return len(self.vertex_at_position)

    def getPosition(self, vertex):
        return self.position_of_vertex[vertex]

    def maximum(self):
        return self.vertex_at_position[0], self.value_at_position[0]

    def findParentPosition(self, position):
        if position == 0:
            return -1
        return int((position - 1) / 2)

    def getVertexAtPosition(self, position):
        return self.vertex_at_position[position]

    def findGreatestChildPosition(self, position):

        if (2 * position) + 1 <= len(self.value_at_position) - 1:
            childPositionLeft = (2 * position) + 1
            if childPositionLeft + 1 <= len(self.value_at_position) - 1:
                childPositionRight = childPositionLeft + 1
            else:
                childPositionRight = -1
            valLeft = self.value_at_position[childPositionLeft]
            valRight = self.value_at_position[childPositionRight]
            if valLeft >= valRight:
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

    def insert(self, vertex_name, value):
        self.value_at_position.append(value)
        self.vertex_at_position.append(vertex_name)
        self.updatePosition(vertex_name, len(self.value_at_position) - 1)
        self.heapify(len(self.value_at_position) - 1)

    def delete(self, vertex_name):
        vertex_position = self.getPosition(vertex_name)
        end_position = len(self.value_at_position) - 1
        self.swap(vertex_position, end_position)

        # self.value_at_position = self.value_at_position[:-1]
        # self.vertex_at_position = self.vertex_at_position[:-1]

        self.value_at_position.pop()
        self.vertex_at_position.pop()
        self.updatePosition(vertex_name, -1)

        if len(self.value_at_position) > 0:
            self.heapify(vertex_position)

    def heapify(self, position):
        heapify_top = False
        parent_position = self.findParentPosition(position)

        while parent_position >= 0 and position <= len(self.value_at_position) - 1:

            if self.value_at_position[parent_position] < self.value_at_position[position]:
                heapify_top = True

                # update vertex and values at both positions
                self.swap(position, parent_position)

                position = parent_position
                parent_position = self.findParentPosition(position)
            else:
                break
        if not heapify_top:
            childPosition = self.findGreatestChildPosition(position)

            while childPosition >= 0:
                bottomHeapify = False

                if self.value_at_position[position] < self.value_at_position[childPosition]:
                    bottomHeapify = True
                    self.swap(position, childPosition)
                    position = childPosition
                    childPosition = self.findGreatestChildPosition(position)
                # else:
                #     childPosition = childPosition + 1
                #     if childPosition <= len(self.value_at_position) - 1:
                #         if self.value_at_position[position] < self.value_at_position[childPosition]:
                #             bottomHeapify = True
                #             self.swap(position, childPosition)
                #             position = childPosition
                #             childPosition = self.findGreatestChildPosition(position)

                if not bottomHeapify:
                    break

    def printHeap(self):
        result = []
        for value in self.value_at_position:
            result.append(value)

        print(result)

    def print_heap(self):
        # str_heap = f"{self.getValue(0)}\n"
        str_heap = f"Heap:\n"
        result = []
        height = int(math.log2(len(self.value_at_position) - 1)) + 1

        for i in range(height):
            start = int(math.pow(2, i) - 1)
            offset = int(math.pow(2, i))
            for j in range(offset):
                try:
                    str_heap += f"  ({start + j}, " \
                                f"{self.position_of_vertex[start + j]}, " \
                                f"{self.vertex_at_position[start + j]}, " \
                                f"{self.value_at_position[start + j]})"
                except:
                    str_heap += ""
            str_heap += "\n"
        return str_heap

    def popMax(self):
        """
        removes max value from the heap and returns the name and value of the removed object.
        :return:
        """
        pop_vertex = self.vertex_at_position[0]
        pop_value = self.value_at_position[0]
        self.delete(pop_vertex)
        return pop_vertex, pop_value


    def heapSort(self):
        n = len(self.value_at_position)

        # Build a maxheap.
        # Since last parent will be at ((n//2)-1) we can start at that location.
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i)

        # One by one extract elements
        sorted_edges = []

