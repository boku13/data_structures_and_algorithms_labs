import sys
sys.setrecursionlimit(2500)

class MetroStop:
    def __init__(self, name, metro_line, fare):
        self.stop_name = name
        self.next_stop = None
        self.prev_stop = None
        self.line = metro_line
        self.fare = fare

    def get_stop_name(self):
        return self.stop_name

    def get_next_stop(self):
        return self.next_stop

    def get_prev_stop(self):
        return self.prev_stop

    def get_line(self):
        return self.line

    def get_fare(self):
        return self.fare

    def set_next_stop(self, next_stop):
        self.next_stop = next_stop

    def set_prev_stop(self, prev_stop):
        self.prev_stop = prev_stop


class MetroLine:
    def __init__(self, name):
        self.line_name = name
        self.node = None

    # Getters and setters for MetroLine class
    def get_line_name(self):
        return self.line_name

    def get_node(self):
        return self.node

    def set_node(self, node):
        self.node = node

    def print_line(self):
        stop = self.node
        while stop is not None:
            # print(stop.get_stop_name())
            print(f"Stop Name: {stop.get_stop_name()}, Metro Line: {stop.get_line()}")
            stop = stop.get_prev_stop() #next to prev
             
    def get_total_stops(self):
        stop = self.node
        total_stops = 0
        while stop is not None:
            total_stops += 1
            stop = stop.get_prev_stop()
        return total_stops

    def populate_line(self, filename):
        stops = []
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                line = line.replace("\n", "")
                line = line.replace(",", "")
                words = line.split()
                stop_name = " ".join(words[:-1])
                stop_fare = words[-1]
                stops.append((stop_name, stop_fare))
                
        metroline = filename.split('.', 1)[0]
        metrostop_prev = None
        for stop_name, stop_fare in stops: 
            metrostop = MetroStop(stop_name, metroline, stop_fare)
            if metrostop_prev is not None:
                metrostop_prev.set_next_stop(metrostop)
            metrostop.set_prev_stop(metrostop_prev)
            metrostop_prev = metrostop
        
        self.node = metrostop_prev  # set the node to the tail node, acts as iterator


class AVLNode:
    def __init__(self, name):
        self.stop_name = name
        self.stops = []
        self.left = None
        self.right = None
        self.parent = None

    def get_stop_name(self):
        return self.stop_name

    def get_stops(self):
        return self.stops

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_parent(self):
        return self.parent

    def add_metro_stop(self, metro_stop):
        self.stops.append(metro_stop)

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_parent(self, parent):
        self.parent = parent


class AVLTree:
    def __init__(self):
        self.root = None
    
    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.right), self.height(node.left))

    def string_compare(self, s1, s2):
        # print("Comparision between :", type(s1), type(s2))
        if s1 > s2:
            return 1
        elif s1 == s2:
            return 0
        else:
            return -1
        
    def balance_factor(self, node):
        return (self.height(node.left) - self.height(node.right))

    def rotate_left(self, node):
        subtree_head = node.right
        x = subtree_head.left
        subtree_head.left = node
        node.right = x
        return subtree_head

    def rotate_right(self, node):
        subtree_head = node.left
        x = subtree_head.right
        subtree_head.right = node
        node.left = x
        return subtree_head
    
    def balance(self, node):
        if node is None:
            return node

        balance = self.balance_factor(node)

        # left heavy
        if balance > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left) #left right additional case
            return self.rotate_right(node) 

        # right heavy
        if balance < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right) 
            return self.rotate_left(node)

        return node

    def insert(self, stop_name, metro_stop):
        self.root = self._insert(self.root, stop_name, metro_stop)

    def _insert(self, node, stop_name, metro_stop):
        if node is None:
            avl_node = AVLNode(stop_name)
            avl_node.stops.append(metro_stop)
            return avl_node
        
        comparision_factor = self.string_compare(stop_name, node.get_stop_name())

        if comparision_factor == -1:
            node.left = self._insert(node.left, stop_name, metro_stop)
        elif comparision_factor == 1:
            node.right = self._insert(node.right, stop_name, metro_stop)
        else:
            node.stops.append(metro_stop)

        return self.balance(node)
    
    def populate_tree(self, metroLine):
        tail = metroLine.node
        while tail is not None:
            #add logic for when the node already exists
            self.insert(tail.stop_name, tail)
            tail = tail.get_prev_stop()
    
    def inOrderTraversal(self, node):
        if node is None:
            return
        self.inOrderTraversal(node.left)
        print(node.stop_name)
        self.inOrderTraversal(node.right)

    # def getTotalNodes(self, node):
    #     total = 0
    #     queue = []
    #     root = self.root
    #     queue.append(root)

    #     while queue:
    #         current_node = queue.pop(0)
    #         total += 1
    #         if current_node.left is not None:
    #             queue.append(current_node.left)
    #         if current_node.right is not None:
    #             queue.append(current_node.right)

    #     return total
    
    def get_total_nodes(self, node):
        if not node:
            return 0
        left_count = self.get_total_nodes(node.left)
        right_count = self.get_total_nodes(node.right)
        return 1 + left_count + right_count
    
    def search_stop(self, stop_name):
        current = self.root
        
        while current:
            # print("Comparing:", current.stop_name, stop_name)
            comparison_factor = self.string_compare(current.stop_name, stop_name)
            if comparison_factor == 1:
                current = current.left
            elif comparison_factor == -1:
                current = current.right
            else:  # comparison_factor == 0
                return current          
    
    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.left, level + 1)
            print(" " * 4 * level + "->", node.stop_name)
            self.printTree(node.right, level + 1)

# Trip class
class Trip:
    def __init__(self, metro_stop, previous_trip):
        self.node = metro_stop
        self.prev = previous_trip

    def get_node(self):
        return self.node

    def get_prev(self):
        return self.prev

# Exploration class
class Exploration:
    def __init__(self):
        self.trips = []

    def get_trips(self):
        return self.trips

    def enqueue(self, trip):
        self.trips.append(trip)

    def dequeue(self):
        if not self.trips:
            return None
        trip = self.trips.pop(0)
        print("Dequeued:", trip.get_node().get_stop_name())
        return trip

    def is_empty(self):
        return not bool(self.trips)
    
    def print_queue(self):
        for trip in self.trips:
            print(f"Stop Name: {trip.get_node().get_stop_name()}, Metro Line: {trip.get_node().get_line()}")


# Path class
class Path:
    def __init__(self):
        self.stops = []
        self.total_fare = 0

    def get_stops(self):
        return self.stops

    def get_total_fare(self):
        return self.total_fare

    def add_stop(self, stop):
        self.stops.append(stop)

    def set_total_fare(self, fare):
        self.total_fare = fare
        
    def compute_fare(self):
        fare = int(self.stops[0].fare) - int(self.stops[len(self.stops)-1].fare) 
        self.total_fare = fare
        return fare

    def print_path(self):
        for stop in self.stops:
            print(f"Stop Name: {stop.get_stop_name()}, Metro Line: {stop.get_line()}")

# PathFinder class
class PathFinder:
    def __init__(self, avl_tree, metro_lines):
        self.tree = avl_tree
        self.lines = metro_lines

    def get_tree(self):
        return self.tree

    def get_lines(self):
        return self.lines

    def create_avl_tree(self):
        for metro_line in self.lines:
            self.tree.populate_tree(metro_line)

    def find_path(self, origin, destination):
        
        #handle the case where the origin can be a junction
        
        paths = []
        
        lines_being_explored = []
        
        forward_exploration = Exploration()
        backward_exploration = Exploration()
        
        origin_stop = self.tree.search_stop(origin)         #avl node
        # print(origin_stop.stop_name)
        # print(origin_stop.stops)
        destination_stop = self.tree.search_stop(destination)    #avl node
        
        # print("chat is this real")
        
        for stop in origin_stop.stops:
            forward_trip = Trip(stop, None) #towards head
            forward_exploration.enqueue(forward_trip)
            backward_trip = Trip(stop, None) #towards tail
            backward_exploration.enqueue(backward_trip)
            print(stop.line)
            lines_being_explored.append(stop.line)
            
            forward_exploration.print_queue()
            backward_exploration.print_queue()    
        
            
        
        while not forward_exploration.is_empty() and not backward_exploration.is_empty():
            #need to make trip objects so that I have a trail to back track on once 
            #i find the destination
            # print("bruh")
            
            forward_search_trip = forward_exploration.dequeue()
            forward_metrostop = forward_search_trip.node        #node here is a metrostop
            
            backward_search_trip = backward_exploration.dequeue()
            backward_metrostop = backward_search_trip.node
            
            forward_exploration.print_queue()
            backward_exploration.print_queue()
            
            while forward_metrostop:
                forward_search_trip = Trip(forward_metrostop, forward_search_trip)
                print("Forward Trip Search in line:", forward_search_trip.node.line)
                print(forward_search_trip.node.stop_name)
                                
                if forward_metrostop.stop_name == destination_stop.stop_name:
                    #make path
                    path = Path()
                    while forward_search_trip.prev:
                        path.add_stop(forward_search_trip.node)
                        forward_search_trip = forward_search_trip.prev
                        # print("Fare until", forward_metrostop.stop_name, " is: ",  path.total_fare)
                        # path.total_fare = path.total_fare + abs(forward_metrostop.fare - forward_metrostop.prev_stop.fare)
                    path.compute_fare()
                    paths.append(path)
                
                forward_metrostop = forward_metrostop.prev_stop
                
                if forward_metrostop:
                    #lines a node is associated with
                    stops_associated = self.tree.search_stop(forward_metrostop.stop_name).stops
                    
                    #the forward search will go ahead with its search in the same line so
                    #its ok to just add the other stops in other lines associated with the avl node to 
                    # exploration
                    
                    if len(stops_associated) > 1:
                        for stop in stops_associated:
                            if stop.line not in lines_being_explored:
                                branch_forward_trip = Trip(stop, forward_search_trip)
                                forward_exploration.enqueue(branch_forward_trip)
                                lines_being_explored.append(stop.line)
                            
            while backward_metrostop:
                backward_search_trip = Trip(backward_metrostop, backward_search_trip)
                print("Backward Trip Search in line:", backward_search_trip.node.line)
 
                print(backward_search_trip.node.stop_name)
                                
                if backward_metrostop.stop_name == destination_stop.stop_name:
                    #make path
                    path = Path()
                    while backward_search_trip.prev:
                        path.add_stop(backward_search_trip.node)
                        # fare_difference = abs(int(backward_metrostop.fare) - int(backward_metrostop.next_stop.fare))
                        # path.total_fare += fare_difference
                        backward_search_trip = backward_search_trip.prev
                    path.compute_fare()
                    paths.append(path)
                
                backward_metrostop = backward_metrostop.next_stop
                
                if backward_metrostop:
                    #lines a node is associated with
                    stops_associated = self.tree.search_stop(backward_metrostop.stop_name).stops
                    
                    #the forward search will go ahead with its search in the same line so
                    #its ok to just add the other stops in other lines associated with the avl node to 
                    # exploration
                    
                    if len(stops_associated) > 1:
                        for stop in stops_associated:
                            if stop.line not in lines_being_explored:
                                branch_backward_trip = Trip(stop, backward_search_trip)
                                backward_exploration.enqueue(branch_backward_trip)
                                lines_being_explored.append(stop.line)
        
        
        # print(paths)
        # for path in paths:
        #     for stop in path.stops:
        #         print(stop.stop_name)
        
        results = sorted(paths, key=lambda x: len(x.stops), reverse=False)
        
        return results[0]
        # paths.sort(key=lambda x: len(x.stops), reverse=False)


lines = [] #metrolines
                   
def main():
    filenames = ["blue.txt", "green.txt", "magenta.txt", "orange.txt", "red.txt", "violet.txt", "yellow.txt"]

    tree = AVLTree()
    for line in filenames:
        metroline = MetroLine(line)
        metroline.populate_line(line)
        tree.populate_tree(metroline)
        lines.append(metroline)
        # metroline.print_line()
        
    # for line in lines:
    #     line.print_line()
    
    # print("Total Nodes:", tree.get_total_nodes(tree.root))
    # print("Height:", tree.height(tree.root))
    # tree.printTree(tree.root)
    # print(tree.height(tree.root))
    
    path_finder = PathFinder(AVLTree(), lines)
    path_finder.create_avl_tree()
    # path_finder.get_tree().printTree(path_finder.get_tree().get_root())
    # print(path_finder.get_tree().search_stop("Janakpuri West")) 
    # path = path_finder.find_path("Pitampura", "Pul Bangash")
    # for stop in path.stops:
    #     print(stop.stop_name)
        
        
    # path = path_finder.find_path("Janakpuri West", "Botanical Garden")
    path = path_finder.find_path("Dwarka Sec-21", "Chawri Bazar") 
    for stop in path.stops:
        print(stop.stop_name)

    
    #TEST THIS MORE.
    
if __name__ == "__main__":
    main()
