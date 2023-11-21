# from scratch max heap
class MaxHeap:
    def _init_(self):
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
        if len(self.heap) == 1:
            return self.heap.pop()
 
        max_item = self.heap[0]
        self.heap[0] = self.heap.pop()
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
        index = len(self.heap) - 1
        while index > 0:
            parent_index = self.parent(index)
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break
 
    def is_empty(self):
        return len(self.heap) == 0
 
 
class Graph:
    def _init_(self):
        self.vertices = {}
 
    def add_edge(self, source, destination, min_freight_cars_to_move, max_parcel_capacity):
        # creates vertices if they don't exist
        # add destination to source's neighbors
        # add source to destination's neighbors
        # each vertex should have a min_freight_cars_to_move and max_parcel_capacity data fields (# this is optional, but recommended for ideal solution)
 
        if source not in self.vertices:
            self.vertices[source] = Vertex(source, min_freight_cars_to_move, max_parcel_capacity)
        if destination not in self.vertices:
            self.vertices[destination] = Vertex(destination, min_freight_cars_to_move, max_parcel_capacity)
 
        self.vertices[source].add_neighbor(destination)
        self.vertices[destination].add_neighbor(source)
 
 
 
 
    def print_graph(self): #optional
        # print(f"Vertex {self.vertices.name}: Neighbors - {', '.join(neighbor.name for neighbor in self.vertices.neighbors)}")
            # complete this function
            pass
 
 
 
    def bfs(self, source, destination):
        # returns a list of vertices in the path from source to destination using BFS
        # actual move might only use next vertex in the path though (careful understanding required)
        visited = set()
        queue = []
        parent_map = {}  # To keep track of the parent vertices in the path
 
        queue.append(source)
        visited.add(source)
 
        while queue:
            current_vertex = queue.pop(0)
 
            if current_vertex == destination:
                # Reconstruct the path from destination to source using parent_map
                path = [destination]
                while path[-1] != source:
                    path.append(parent_map[path[-1]])
                return path[::-1]  # Reverse the path to start from source
 
            for neighbor in self.vertices[current_vertex].neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    parent_map[neighbor] = current_vertex  # Set the parent of the neighbor
 
        return []
 
 
        # Inside the Graph class
    def dfs(self, source, destination):
        visited = set()
        stack = []
        parent_map = {}  # To keep track of the parent vertices in the path
 
        stack.append(source)
        visited.add(source)
 
        while stack:
            current_vertex = stack.pop()
 
            if current_vertex == destination:
                # Reconstruct the path from destination to source using parent_map
                path = [destination]
                while path[-1] != source:
                    path.append(parent_map[path[-1]])
                return path[::-1]  # Reverse the path to start from source
 
            for neighbor in self.vertices[current_vertex].neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
                    parent_map[neighbor] = current_vertex  # Set the parent of the neighbor
 
        return []  # Return an empty list if no path is found
 
 
 
    def groupFreightCars(self):
        # group freight cars at every vertex based on their destination
 
        for vertex in self.vertices.values():
            vertex.groupFreightCars()
 
 
 
    def moveTrains(self):
        # move trains  (constitutes one time tick)
        # a train should move only if has >= min_freight_cars_to_move freight cars to link (link is a vertex, obtained from bfs or dfs)
        # once train moves from the source vertex, all the freight cars should be sealed and cannot be unloaded (at any intermediate station) until they reach their destination
        # check if there are enough freight cars to move
        for source in self.vertices:
            # If there are enough freight cars to move
            if len(self.vertices[source].freight_cars) >= self.vertices[source].min_freight_cars_to_move:
                # Get the vertices to link using BFS or DFS
                vertices_to_link = self.bfs(source, destination)  # Implement bfs or dfs as per your logic
 
                # Move trains from source vertex to destination vertex
                for destination in vertices_to_link:
                    path = self.dfs(source, destination)  # Implement dfs as per your logic
                    if path:
                        for vertex in path:
                            vertex.moveTrains()
                            vertex.sealFreightCars()
        return
 
 
class Vertex:
    def _init_(self, name, min_freight_cars_to_move, max_parcel_capacity):
 
 
        self.name = name
        self.freight_cars = []
        self.neighbors = []
        self.trains_to_move = None
        self.min_freight_cars_to_move = min_freight_cars_to_move
        self.max_parcel_capacity = max_parcel_capacity
        self.parcel_destination_heaps = {}
        self.sealed_freight_cars = []
 
        self.all_parcels = []
 
    def add_neighbor(self, neighbor):
        # add neighbor to self.neighbors
        self.neighbors.append(neighbor)
 
 
    def get_all_current_parcels(self):
        # return all parcels at the current vertex
        return self.all_parcels
 
 
    def clean_unmoved_freight_cars(self):
        # remove all freight cars that have not moved from the current vertex
        # add all parcels from these freight cars back to the parcel_destination_heaps accoridingly
 
        for freight_car in self.freight_cars:
            if freight_car.can_move() == False:
                for parcel in freight_car.parcels:
                    self.parcel_destination_heaps[parcel.destination].insert(parcel)
                self.freight_cars.remove(freight_car)
        pass
 
    def loadParcel(self, parcel):
        # load parcel into parcel_destination_heaps based on parcel.destination
        self.parcel_destination_heaps.setdefault(parcel.destination, MaxHeap()).insert(parcel)
        pass
 
 
    def loadFreightCars(self):
        # load parcels onto freight cars based on their destination
        # remember a freight car is allowed to move only if it has exactly max_parcel_capacity parcels
        # create a list to store the freight cars that can move
        movable_freight_cars = []
 
        # iterate over all the freight cars
        for freight_car in self.freight_cars:
            # check if the freight car has exactly max_parcel_capacity parcels
            if len(freight_car.parcels) == self.max_parcel_capacity:
                # add the freight car to the list of movable freight cars
                movable_freight_cars.append(freight_car)
 
        # iterate over the movable freight cars
        for freight_car in movable_freight_cars:
            # move the freight car to the next vertex
            freight_car.move(self)
 
        return
 
 
 
    def print_parcels_in_freight_cars(self):
        # optional method to print parcels in freight cars
 
            # optional method to print parcels in freight cars
            pass
 
 
 
class FreightCar:
    def _init_(self, max_parcel_capacity):
 
        self.max_parcel_capacity = max_parcel_capacity
        self.parcels = []
        self.destination_city = None
        self.next_link = None
        self.current_location = None
        self.sealed = False
 
    def load_parcel(self, parcel):
        # load parcel into freight car
        self.parcels.append(parcel)
        pass
 
    def can_move(self):
        # return True if freight car can move, False otherwise
        return len(self.parcels) == self.max_parcel_capacity
 
 
 
    def move(self, destination):
        # update current_location
        # empty the freight car if destination is reached, set all parcels to delivered
        if self.current_location == destination:
            self.parcels = []
            for parcel in self.parcels:
                parcel.delivered = True
 
 
 
 
class Parcel:
    def _init_(self, time_tick, parcel_id, origin, destination, priority):
        self.time_tick = time_tick
        self.parcel_id = parcel_id
        self.origin = origin
        self.destination = destination
        self.priority = priority
        self.delivered = False
        self.current_location = origin
 
class PRC:
    def _init_(self, min_freight_cars_to_move=5, max_parcel_capacity=5):
        self.graph = Graph()
        self.freight_cars = []
        self.parcels = {}
        self.parcels_with_time_tick = {}
        self.min_freight_cars_to_move = min_freight_cars_to_move
        self.max_parcel_capacity = max_parcel_capacity
        self.time_tick = 1
 
        self.old_state = None
        self.new_state = None
 
        self.max_time_tick = 10
 
        # self.create_graph('samples/1/graph.txt')
        # self.process_parcels('samples/5/bookings.txt')
 
 
    def get_state_of_parcels(self):
        return {x.parcel_id:x.current_location for x in self.parcels.values()}
 
 
    def process_parcels(self, booking_file_path):
        with open(booking_file_path, 'r') as file:
            lines = file.readlines()
            for line in lines[1:]:
                elements = line.strip().split()
                time_tick, parcel_id, origin, destination, priority = map(str, elements)
                parcel = Parcel(time_tick, parcel_id, origin, destination, priority)
                self.parcels[parcel_id] = parcel
 
                if time_tick not in self.parcels_with_time_tick:
                    self.parcels_with_time_tick[time_tick] = []
 
                self.parcels_with_time_tick[time_tick].append(parcel)
 
    def getNewBookingsatTimeTickatVertex(self, time_tick, vertex):
        # return all parcels at time tick and vertex
        pass
 
 
 
    def run_simulation(self, run_till_time_tick=None):
        # run simulation till run_till_time_tick if provided, if not run till max_time_tick
        # if convergence is achieved (before run_till_time_tick or max_time_tick), stop simulation
        # convergence is state of parcels in the system does not change from one time tick to the next, and there are no further incoming parcels in next time ticks
 
        bookings = self.getNewBookingsatTimeTickatVertex(self.time_tick, None)
        for vertex in self.graph.vertices:
            parcels_at_vertex = self.getNewBookingsatTimeTickatVertex(self.time_tick, vertex)
            vertex.loadParcel(parcels_at_vertex)
 
        self.graph.groupFreightCars()
        self.graph.moveTrains()
        self.time_tick += 1
 
 
 
    def convergence_check(self, previous_state, current_state):
        # return True if convergence achieved, False otherwise
        # check if previous_state and current_state are equal
 
            return True
 
 
 
    def all_parcels_delivered(self):
        return all(parcel.delivered for _,parcel in self.parcels.items())
 
    def delivered_parcels(self):
        return [parcel.parcel_id for parcel in self.parcels.values() if parcel.delivered]
 
    def get_stranded_parcels(self):
        return [parcel.parcel_id for parcel in self.parcels.values() if not parcel.delivered]
 
    def status_of_parcels_at_time_tick(self, time_tick):
        return [parcel.parcel_id for parcel in self.parcels.values() if parcel.time_tick <= time_tick and not parcel.delivered]
 
    def status_of_parcel(self, parcel_id):
        return self.parcels[parcel_id].delivered, self.parcels[parcel_id].current_location
 
    def create_graph(self, graph_file_path):
        # read graph.txt and create graph
        with open(graph_file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                elements = line.strip().split()
                source, destination = map(str, elements)
                self.graph.add_edge(source, destination, self.min_freight_cars_to_move, self.max_parcel)
 
 
# if _name_ == "_main_":
 
#     min_freight_cars_to_move = 2
#     max_parcel_capacity = 2
 
#     prc = PRC(min_freight_cars_to_move, max_parcel_capacity)
 
#     prc.run_simulation()
 
#     print(f'All parcels delivered: {prc.all_parcels_delivered()}')
#     print(f'Delivered parcels: {prc.delivered_parcels()}')
#     print(f'Stranded parcels: {prc.get_stranded_parcels()}')