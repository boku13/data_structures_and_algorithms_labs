import heapq


class Item:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def __lt__(self, other):
        # Custom comparison for the heapq
        return self.priority < other.priority

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, vertex):
        heapq.heappush(self.heap, vertex)

    def pop(self):
        return heapq.heappop(self.heap)

    def get_max(self):
        if self.heap:
            return self.heap[0]
        return None

    def extract_max(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def is_empty(self):
        return not bool(self.heap)

# # Example usage:
# vertex1 = Vertex("A", 4)
# vertex2 = Vertex("B", 8)
# vertex3 = Vertex("C", 2)
# vertex4 = Vertex("D", 5)

# max_heap = MaxHeap()
# max_heap.push(vertex1)
# max_heap.push(vertex2)
# max_heap.push(vertex3)
# max_heap.push(vertex4)

# print("Max Heap:")
# for vertex in max_heap.heap:
#     print(f"Vertex {vertex.name}: Priority {vertex.priority}")

# print("\nMax Vertex:")
# max_vertex = max_heap.extract_max()
# print(f"Vertex {max_vertex.name}: Priority {max_vertex.priority}")

# print("\nMax Heap after extraction:")
# for vertex in max_heap.heap:
#     print(f"Vertex {vertex.name}: Priority {vertex.priority}")


# Test Case 1: Insertion and Extraction
heap = MaxHeap()
elements_to_insert = [(3, 'C'), (1, 'A'), (4, 'D'), (2, 'B')]
expected_order = ['D', 'C', 'B', 'A']

for priority, value in elements_to_insert:
    heap.insert(Item(priority, value))

result_order = []
while not heap.is_empty():
    result_order.append(heap.extract_max().value)
    
print(result_order)

print(expected_order)

assert result_order == expected_order

# Test Case 2: Empty Heap Extraction
empty_heap = MaxHeap()
try:
    empty_heap.extract_max()
    # If the above line doesn't raise an exception, the test fails
    assert False, "Expected IndexError but no exception was raised."
except IndexError as e:
    pass  # Expected behavior

# Test Case 3: Check if Heap is Empty
heap = MaxHeap()
elements_to_insert = [(3, 'C'), (1, 'A'), (4, 'D'), (2, 'B')]

for priority, value in elements_to_insert:
    heap.insert(Item(priority, value))

while not heap.is_empty():
    heap.extract_max()

assert heap.is_empty()

# Test Case 4: Random Insertion and Extraction
import random

heap = MaxHeap()
elements_to_insert = [(random.randint(1, 100), str(i)) for i in range(100)]

for priority, value in elements_to_insert:
    heap.insert(Item(priority, value))

sorted_elements = sorted(elements_to_insert, key=lambda x: x[0], reverse=True)
expected_order = [value for priority, value in sorted_elements]

result_order = []
while not heap.is_empty():
    result_order.append(heap.extract_max().value)
     
print(result_order)
print(expected_order)

assert result_order == expected_order