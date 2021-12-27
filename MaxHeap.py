import math


class MaxHeap:

    def __init__(self, numOfVertices):
        self.numVertices = numOfVertices
        self.heapArray = [-1 for i in range(numOfVertices)]
        self.valueArray = [-1 for i in range(numOfVertices)]
        self.positionArray = [-1 for i in range(numOfVertices)]
        self.indexArray = [-1 for i in range(numOfVertices)]
        self.endPosition = 0
        self.lastIndex = -1

    def insert(self, vertexName, value):
        self.updateIndex(vertexName, self.endPosition)
        self.updateHeap(self.endPosition, vertexName)
        self.updatePosition(vertexName, self.endPosition)
        self.updateValue(vertexName, value)
        self.heapify(self.endPosition)
        self.endPosition += 1
        self.lastIndex += 1

    def delete(self, vertex):
        self.endPosition -= 1
        # get the index of vertex
        temp = self.getIndex(vertex)
        position = self.getPosition(vertex)
        tempEndVertex = self.getVertex(self.endPosition)

        # swap heap
        self.swapHeap(position, self.endPosition)
        print(f"after swapHeap: {self.print_heap()}")

        # swap position
        self.swapPosition(vertex, tempEndVertex)
        print(f"after swapPosition: {self.print_heap()}")

        self.updatePosition(vertex, self.positionArray[self.endPosition])
        print(f"after updatePosition: {self.print_heap()}")

        # index which is free - 5
        # index assigned to last vertex name - 11
        # need assigned to last index - 9 - > vertex
        self.updateValue(vertex, self.valueArray[self.endPosition])
        print(f"after updateValue: {self.print_heap()}")

        # update the index of vertex in the index array to -1 to indicate that this vertex does not exist
        self.updateIndex(vertex, -1)
        print(f"after updateIndex: {self.print_heap()}")

        # get the last element in the heap and update its index position to the position in step 1
        # self.updateIndex(self.lastIndex, temp)
        self.updateIndex(self.lastIndex, temp)
        print(f"after updateIndex 2nd: {self.print_heap()}")

        self.heapArray[self.endPosition] = -1
        self.positionArray[self.endPosition] = -1
        self.valueArray[self.endPosition] = -1

        self.heapify(position)

        # update heap array[position] = name of the vertex in the last

        # position[ index of the vertex] = last element's position
        # value[index of the vertex] = last elements value
        pass

    def heapify(self, position):
        heapifyTop = False
        parentPosition = self.findParentPosition(position)

        while parentPosition >= 0:
            if self.getValue(parentPosition) < self.getValue(position):
                heapifyTop = True
                self.swapHeap(position, parentPosition)
                self.swapPosition(self.getVertex(position), self.getVertex(parentPosition))
                position = parentPosition
                parentPosition = self.findParentPosition(position)
            else:
                break
        if not heapifyTop:
            childPosition = self.findLeftChild(position)

            while childPosition >= 0:
                bottomHeapify = False
                if self.getValue(position) < self.getValue(childPosition):
                    bottomHeapify = True
                    self.swapHeap(position, childPosition)
                    self.swapPosition(self.getVertex(position), self.getVertex(childPosition))
                    position = childPosition
                    childPosition = self.findLeftChild(position)
                else:
                    childPosition = childPosition + 1
                    if childPosition <= self.endPosition:
                        if self.getValue(position) < self.getValue(childPosition):
                            bottomHeapify = True
                            self.swapHeap(position, childPosition)
                            self.swapPosition(self.getVertex(position), self.getVertex(childPosition))
                            position = childPosition
                            childPosition = self.findLeftChild(position)

                if not bottomHeapify:
                    break

    #     write the logic of heapify in case delete as well
    # check if the child at this position exists
    # get the child vertex (left and right if exists) and see if it greater than the parent
    # swap heap and swap position. do we need to swap value??
    # continue this till we get no further children
    # else break

    def maximum(self):
        return self.getValue(0)

    def findParentPosition(self, position):
        if position == 0:
            return -1
        return int((position - 1) / 2)

    def findLeftChild(self, position):
        if (2 * position) + 1 <= self.endPosition:
            return (2 * position) + 1
        else:
            return -1

    def updateHeap(self, position, key):
        self.heapArray[position] = key

    def getVertex(self, position):
        return self.heapArray[position]

    def updateValue(self, vertexName, value):
        index = self.indexArray[vertexName]
        self.valueArray[index] = value

    def getValue(self, position):
        """
        Given a position, finds the vertex and its index position which will point to its value.
        :param position:
        :return:
        """
        return self.valueArray[self.getIndex(self.getVertex(position))]

    def getPosition(self, vertexName):
        index = self.getIndex(vertexName)
        return self.positionArray[index]

    def updatePosition(self, vertexName, position):
        index = self.getIndex(vertexName)
        self.positionArray[index] = position

    def swapHeap(self, position1, position2):
        self.heapArray[position1], self.heapArray[position2] = self.heapArray[position2], self.heapArray[position1]

    def swapPosition(self, vertex1, vertex2):
        index1 = self.getIndex(vertex1)
        index2 = self.getIndex(vertex2)
        self.positionArray[index1], self.positionArray[index2] = self.positionArray[index2], self.positionArray[index1]

    def getIndex(self, vertex):
        """
        given the name of the vertex, returns the index of that vertex to access the Position and values arrays
        :param vertex:
        :return:
        """
        return self.indexArray[vertex]

    def updateIndex(self, vertex, index):
        """
        gives the index or key value to access the Position and Value arrays
        :param vertex:
        :param index:
        :return:
        """
        self.indexArray[vertex] = index

    def printHeap(self):

        result = []
        for i in range(0, self.endPosition):
            result.append(self.getValue(i))
        return result

    def print_heap(self):
        # str_heap = f"{self.getValue(0)}\n"
        str_heap = f"Heap:\n"
        result = []
        height = int(math.log2(self.endPosition)) + 1

        for i in range(height):
            start = int(math.pow(2, i) - 1)
            offset = int(math.pow(2, i))
            for j in range(offset):
                try:
                    str_heap += f"  ({start + j}, " \
                                f"{self.heapArray[start+j]}, " \
                                f"{self.getIndex(self.heapArray[start+j])}, " \
                                f"{self.getValue(start + j)})"
                except:
                    str_heap += ""
            str_heap += "\n"
        return str_heap
