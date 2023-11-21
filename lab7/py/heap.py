# # from scratch max heap
# class MaxHeap:
#     def __init__(self):
#         self.heap = []

#     def parent(self, i):
#         return (i - 1) // 2

#     def left(self, i):
#         return 2 * i + 1

#     def right(self, i):
#         return 2 * i + 2

#     def get_max(self):
#         if self.is_empty():
#             raise IndexError("Heap is empty")
#         return self.heap[0].priority
    
#     def extract_max(self):
#         if self.is_empty():
#             raise IndexError("Heap is empty")

#         max_item = self.heap[0]
#         last_item = self.heap.pop()

#         if self.heap:
#             self.heap[0] = last_item
#             self.max_heapify(0)

#         return max_item


#     def max_heapify(self, i):
#         left_child = self.left(i)
#         right_child = self.right(i)
#         largest = i

#         if left_child < len(self.heap) and self.heap[left_child].priority > self.heap[largest].priority:
#             largest = left_child

#         if right_child < len(self.heap) and self.heap[right_child].priority > self.heap[largest].priority:
#             largest = right_child

#         if largest != i:
#             self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
#             self.max_heapify(largest)

#     def insert(self, item):
#         self.heap.append(item)
#         index = len(self.heap) - 1

#         while index > 0:
#             parent_index = self.parent(index)
#             if self.heap[index].priority > self.heap[parent_index].priority:
#                 self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
#                 index = parent_index
#             else:
#                 break

#     def is_empty(self):
#         return len(self.heap) == 0
    
    
class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def get_max(self):
        if self.heap:
            return self.heap[0]
        return None

    def extract_max(self):
        if not self.heap:
            return None

        max_item = self.heap[0]
        last_item = self.heap.pop()
        
        if self.heap:
            self.heap[0] = last_item
            self.max_heapify(0)

        return max_item

    def max_heapify(self, i):
        left_child = self.left(i)
        right_child = self.right(i)
        largest = i

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child

        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def insert(self, item):
        self.heap.append(item)
        i = len(self.heap) - 1

        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def is_empty(self):
        return not bool(self.heap)
    

class Item:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value
    
    def __lt__(self, other):
        # Custom comparison 
        return self.priority < other.priority


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
expected_order = [priority for priority, value in sorted_elements]

result_order = []
while not heap.is_empty():
    result_order.append(heap.extract_max().priority)
     
print(result_order)
print(expected_order)

assert result_order == expected_order


