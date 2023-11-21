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
    

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

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
        self.edges.append((source, destination))

    def print_graph(self): #optional
        for vertex, neighbors in self.vertices.items():
            print(f"Vertex: {vertex}")
            # print(f"Neighbors: {', '.join(neighbors)}")
            print(f"Neighbors: {', '.join(neighbors.neighbors)}")
            print()
    
    def print_vertices(self):
        for vertex in self.vertices:
            print(vertex)
    
    def print_graph_edges(self): #optional
        for edge in self.edges:
            print("-".join(edge))

    def bfs(self, source, destination):
        # returns a list of vertices in the path from source to destination using BFS
        # actual move might only use next vertex in the path though (careful understanding required)
        visited = set()
        queue = [[source]]

        if source == destination:
            return [source]

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node not in visited:
                neighbors = self.vertices[node].neighbors
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

                    if neighbor == destination:
                        return new_path

                visited.add(node)
                
                
    def dfs(self, source, destination):
        # returns a list of vertices in the path from source to destination using DFS
        # actual move might only use next vertex in the path though (careful understanding required)
        # ordering of vertices is important, create vertices in the order they are seen in the input file
        visited = set()

        def dfs_recursive(current_vertex, path):
            if current_vertex == destination:
                return path

            if current_vertex not in visited:
                visited.add(current_vertex)
                for neighbor in self.vertices[current_vertex].neighbors:
                    if neighbor not in visited:
                        result = dfs_recursive(neighbor, path + [neighbor])
                        if result:
                            return result

            return []

        return dfs_recursive(source, [source])

    def bfs_link(self, vertex, destination_city):
        return self.bfs(vertex.name, destination_city)[1]
    
    
    def groupFreightCars(self):
        # group freight cars at every vertex based on their destination
        for vertex in self.vertices.values(): 
            print(vertex.name)
            print(vertex.freight_cars_can_move)
            for destination_city, cars in vertex.freight_cars_can_move.items():
                print(f" Destination : {destination_city} ")
                print(len(cars))
                if len(cars) >= vertex.min_freight_cars_to_move:
                    print(f"Searching for Bfs link from {vertex.name}  to {destination_city}")
                    link = self.bfs_link(vertex, destination_city)
                    print(f"Next Link : {link}")
                    for car in cars:
                        if link not in vertex.trains_to_move:
                            vertex.trains_to_move[link] = []
                        vertex.trains_to_move[link].append(car)
            
                else: 
                    link = self.dfs(vertex.name, destination_city)


    def moveTrains(self):
        # move trains  (constitutes one time tick)
        # a train should move only if has >= min_freight_cars_to_move freight cars to link (link is a vertex, obtained from bfs or dfs)
        # once train moves from the source vertex, all the freight cars should be sealed and cannot be unloaded (at any intermediate station) until they reach their destination
        for vertex in self.vertices.values():
            for link, cars in vertex.trains_to_move.items():
                for car in cars:
                    car.move(link)                    
                    if car.sealed == False:
                        car.sealed = True
                    if car not in vertex.sealed_freight_cars:    
                        vertex.sealed_freight_cars.append(car)
                    self.vertices[link].freight_cars.append(car)
            vertex.freight_cars = [car for car in vertex.freight_cars if car.current_location == vertex.name]
            vertex.freight_cars_can_move.clear()
            vertex.trains_to_move.clear()

        
    
    def train_can_move(self):
        pass


class Vertex:   #done
    def __init__(self, name, min_freight_cars_to_move, max_parcel_capacity):


        self.name = name
        self.freight_cars = []
        self.neighbors = []
        self.freight_cars_can_move = {} #since bfs path remains the same so the next vertex is more or less fixed
        
        self.trains_to_move = {}
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
    
    def clean_unmoved_freight_cars(self):   #done
        # remove all freight cars that have not moved from the current vertex
        # add all parcels from these freight cars back to the parcel_destination_heaps accoridingly
        #after each time-tick?
        for freight_car in self.freight_cars:
            if freight_car.current_location == self.name:   #necessary?
                self.freight_cars.remove(freight_car)
                for parcel in freight_car.parcels:
                    self.loadParcel(parcel)
        

    def loadParcel(self, parcel):   #done
        # load parcel into parcel_destination_heaps based on parcel.destination
        if parcel.destination not in self.parcel_destination_heaps:
            self.parcel_destination_heaps[parcel.destination] = MaxHeap()
        self.parcel_destination_heaps[parcel.destination].insert(parcel)
        self.all_parcels.append(parcel) 
    

    def loadFreightCars(self):  #done
        # load parcels onto freight cars based on their destination
        # remember a freight car is allowed to move only if it has exactly max_parcel_capacity parcels
        for destination, heap in self.parcel_destination_heaps.items():
            # print("destination", destination)
            while heap.is_empty() == False:
                # print("outer", len(heap.heap))
                freight_cars = []
                freight_car = FreightCar(self.max_parcel_capacity)
                freight_car.destination_city = destination
                # i = 0
                while len(freight_car.parcels) < self.max_parcel_capacity and heap.is_empty() == False:
                    # i+=1
                    # print(i)
                    # print(heap.get_max())
                    # print(heap.get_max().parcel_id)
                    # print(heap.get_max().priority)
                    freight_car.load_parcel(heap.extract_max())
                self.freight_cars.append(freight_car)
            # print("1--------------------------------------------------")  
            # print(self.freight_cars)
            # print("1--------------------------------------------------")  
                # self.trains_to_move[destination].append(freight_cars) gotta use this in graph group method
              
    def group_freight_cars(self):
        for car in self.freight_cars:
            if car.can_move():
                if car.destination_city not in self.freight_cars_can_move:
                    self.freight_cars_can_move[car.destination_city] = []
                self.freight_cars_can_move[car.destination_city].append(car)      

    def print_parcels_in_freight_cars(self):
        # optional method to print parcels in freight cars
        pass
        

class FreightCar:   #done
    def __init__(self, max_parcel_capacity):

        self.max_parcel_capacity = max_parcel_capacity
        self.parcels = []
        self.destination_city = None
        self.next_link = None
        self.current_location = None
        self.sealed = False
        self.origin = None #remove if this messes with anything else
        
    def load_parcel(self, parcel):
        # load parcel into freight car
        self.parcels.append(parcel)
        self.origin = parcel.origin
        self.destination = parcel.destination

    def can_move(self):
        # return True if freight car can move, False otherwise
        if len(self.parcels) == self.max_parcel_capacity:
            return True
        else:
            return False
        
    def move(self, destination):
        # update current_location
        # empty the freight car if destination is reached, set all parcels to delivered
        # if self.current_location == self.destination_city:
        self.current_location = destination
        for parcel in self.parcels:
            parcel.current_location = destination   #des - link
        if self.current_location == self.destination_city:
            for parcel in self.parcels:
                parcel.delivered = True
        print("empty check:")
        self.parcels.clear()
        print(self.parcels)
        


class Parcel:
    def __init__(self, time_tick, parcel_id, origin, destination, priority):
        self.time_tick = time_tick
        self.parcel_id = parcel_id
        self.origin = origin
        self.destination = destination
        self.priority = priority
        self.delivered = False
        self.current_location = origin
        
    def __lt__(self, other):
        # Custom comparison 
        return self.priority < other.priority

class PRC:
    def __init__(self, min_freight_cars_to_move=5, max_parcel_capacity=5):
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
    
    def get_state_of_parcels(self):
        return {x.parcel_id:x.current_location for x in self.parcels.values()}
        

    def process_parcels(self, booking_file_path):
        # read bookings.txt and create parcels, populate self.parcels_with_time_tick (dict with key as time_tick and value as list of parcels)
        # and self.parcels (dict with key as parcel_id and value as parcel object)
        with open(booking_file_path, 'r') as file:
            for line in file:
                data = line.strip().split()
                time_tick, parcel_id, origin, destination, priority = map(str, data)
                priority = int(priority)
                time_tick = int(time_tick)
                parcel = Parcel(time_tick, parcel_id, origin, destination, priority)
                self.parcels[parcel_id] = parcel
                if time_tick not in self.parcels_with_time_tick:
                    self.parcels_with_time_tick[time_tick] = []
                self.parcels_with_time_tick[time_tick].append(parcel)            
            
    
    def getNewBookingsatTimeTickatVertex(self, time_tick, vertex):
        # return all parcels at time tick and vertex
        bookings = []
        for parcel in self.parcels.values():
            if parcel.time_tick == time_tick and parcel.origin == vertex:
                bookings.append(parcel)
        return bookings

    

    def run_simulation(self, run_till_time_tick=None):
        # run simulation till run_till_time_tick if provided, if not run till max_time_tick
        # if convergence is achieved (before run_till_time_tick or max_time_tick), stop simulation
        # convergence is state of parcels in the system does not change from one time tick to the next, and there are no further incoming parcels in next time ticks
        if run_till_time_tick is not None:
            self.max_time_tick = run_till_time_tick
        
        # while self.time_tick <= self.max_time_tick:
        while self.time_tick <= 3:
            
            self.old_state = self.new_state
            self.new_state = self.get_state_of_parcels()
            print(f"TIME TICK TIME TIME TICK : {self.time_tick} ----------------------------")
            print("---------------------------------------------------")      
        
            if self.time_tick in self.parcels_with_time_tick:
                for parcel in self.parcels_with_time_tick[self.time_tick]:
                    new_bookings = self.getNewBookingsatTimeTickatVertex(self.time_tick, parcel.origin)
                    vertex = self.graph.vertices[parcel.origin]
                    vertex.loadParcel(parcel)
                      
            for vertex in self.graph.vertices.values():
                vertex.clean_unmoved_freight_cars() #check if this working
                vertex.loadFreightCars()
                vertex.group_freight_cars()

            self.graph.groupFreightCars()  
            self.graph.moveTrains()
            
            if self.convergence_check(self.old_state, self.new_state):
                break
            
            self.time_tick += 1
        

    def convergence_check(self, previous_state, current_state):
        # return True if convergence achieved, False otherwise
        
        pass

    def all_parcels_delivered(self):
        return all(parcel.delivered for _,parcel in self.parcels.items())
    
    def get_delivered_parcels(self):
        return [parcel.parcel_id for parcel in self.parcels.values() if parcel.delivered]
    
    def get_stranded_parcels(self):
        return [parcel.parcel_id for parcel in self.parcels.values() if not parcel.delivered]

    def status_of_parcels_at_time_tick(self, time_tick):
        return [(parcel.parcel_id, parcel.current_location, parcel.delivered) for parcel in self.parcels.values() if parcel.time_tick <= time_tick and not parcel.delivered]
    
    def status_of_parcel(self, parcel_id):
        return self.parcels[parcel_id].delivered, self.parcels[parcel_id].current_location

    def get_parcels_delivered_upto_time_tick(self, time_tick):
        return [parcel.parcel_id for parcel in self.parcels.values() if parcel.time_tick <= time_tick and parcel.delivered]

    def create_graph(self, graph_file_path):
        with open(graph_file_path, 'r') as file:
            # print(file)
            for line in file:
                data = line.strip().split()
                source, destination = map(str, data)
                self.graph.add_edge(source, destination, self.min_freight_cars_to_move, self.max_parcel_capacity)


if __name__ == "__main__":
    
    min_freight_cars_to_move = 2
    max_parcel_capacity = 2

    prc = PRC(min_freight_cars_to_move, max_parcel_capacity)

    prc.create_graph('samples/5/graph.txt')
    prc.process_parcels('samples/5/bookings.txt')

    prc.run_simulation()

    print(f'All parcels delivered: {prc.all_parcels_delivered()}')
    print(f'Delivered parcels: {prc.get_delivered_parcels()}')
    print(f'Stranded parcels: {prc.get_stranded_parcels()}')
    
    # # #my stuff
    # prc_n = PRC(5,5)
    # # create a graph
    # prc_n.create_graph('samples/2/graph.txt')
    # prc_n.process_parcels('samples/2/bookings.txt')
    # print(prc.graph.vertices)
    # prc_n.graph.print_graph()
    # prc_n.graph.print_graph_edges()
    # # prc_n.graph.print_vertices()  
    # # print(len(prc_n.graph.vertices))
    # print(len(prc_n.graph.edges))
    
    
    #     # create a PRC object
    # prc = PRC(2, 2)
    # # create a graph
    # prc.create_graph('samples/2/graph.txt')
    # prc.process_parcels('samples/2/bookings.txt')
    # prc.run_simulation(3)
    # assert prc.all_parcels_delivered() == False
    # assert 'P2Ludhiana4' in prc.get_stranded_parcels()

    # prc.run_simulation(4)
    # print(prc.get_stranded_parcels())
    # assert 'P2Ludhiana4' not in prc.get_stranded_parcels()