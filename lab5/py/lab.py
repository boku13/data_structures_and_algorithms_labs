class MetroStop:
    def __init__(self, name, metroLine, fare):
        self.stopName = name
        self.nextStop = None
        self.prevStop = None
        self.line = metroLine
        self.fare = fare

    def getStopName(self):
        return self.stopName

    def getNextStop(self):
        return self.nextStop

    def getPrevStop(self):
        return self.prevStop

    def getLine(self):
        return self.line

    def getFare(self):
        return self.fare

    def setNextStop(self, next):
        self.nextStop = next

    def setPrevStop(self, prev):
        self.prevStop = prev


class MetroLine:
    def __init__(self, name):
        self.lineName = name
        self.node = None

    def getLineName(self):
        return self.lineName

    def getNode(self):
        return self.node

    def setNode(self, node):
        self.node = node

    def printLine(self):
        stop = self.node
        while stop is not None:
            print(stop.getStopName())
            stop = stop.getNextStop()

    def getTotalStops(self):
        pass

    def populateLine(self, filename):
        #for each line in the file, make a node and set the next to the next node:
        stops = read_file(filename)
        metroline = filename.split('.', 1)[0]
        metrostop_prev = None
        for stop_name, stop_fare in stops:
            metrostop = MetroStop(stop_name, metroline, stop_fare)
            if metrostop_prev is not None:
                metrostop_prev.setNextStop(metrostop)
            metrostop.setPrevStop(metrostop_prev)
            metrostop_prev = metrostop
        self.node = metrostop_prev #set the node to the tail node, acts as iterator
            

class AVLNode:
    def __init__(self, name):
        self.stopName = name
        self.stops = []
        self.left = None
        self.right = None
        self.parent = None

    def getStopName(self):
        return self.stopName

    def getStops(self):
        return self.stops

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getParent(self):
        return self.parent

    def addMetroStop(self, metroStop):
        self.stops.append(metroStop)


class AVLTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def setRoot(self, root):
        self.root = root

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.right) , self.height(node.left))

    def balanceFactor(self, node):
        return (self.height(node.left) - self.height(node.right))

    def rotateLeft(self, node):
        subtreehead = node.right
        x = subtreehead.left
        subtreehead.left = node
        node.right = x
        return subtreehead

    def rotateRight(self, node):
        subtreehead = node.left 
        x = subtreehead.right
        subtreehead.right = node
        node.left = x
        return subtreehead

    def balance(self, node):
        bf = self.balanceFactor(node)
        
        if bf > 1 and node.left.left is not None:
            node.left = self.rotateRight(node)
        if bf < -1 and node.right.right is not None:
            return self.rotateLeft(node)
        elif 

    def stringCompare(self, s1, s2):
        if (s1 > s2): return 1
        if (s1 == s2): return 0
        if (s1 < s2 ): return -1
        
    def insert(self, node, metroStop):
        #here, the node belongs to the linked list
        avl_node = AVLNode(metroStop.stopName)
        avl_node.stops.append(metroStop)
        if not self.root:
            self.root = avl_node
            return
        
        current = self.root
        
        while current:
            parent = current
            comparision_factor = self.stringCompare(current.stopName, node.stopName)
            if comparision_factor == 1:
                cuurent = cuurent.left
            elif comparision_factor == -1:
                current = current.right
            elif comparision_factor == 0:
                current.stops.append(metroStop)
                return
            
        comparision_factor = self.stringCompare(parent.stopName, node.stopName)
        if comparision_factor == 1:
            parent.left = avl_node
        elif comparision_factor == -1:
            parent.right = avl_node
            
        
    def populateTree(self, metroLine):
        tail = metroLine.node
        while tail.getPrevStop() is not None:
            #add logic for when the node already exists
            self.insert(tail)
            tail = tail.getPrevStop()
        
    def in_order_traversal(self, node):
        if node is None:
            return
        self.in_order_traversal(node.get_left())
        print(node.get_stop_name())
        self.in_order_traversal(node.get_right())

    def getTotalNodes(self, node):
        total = 0
        queue = []
        root = self.root
        queue.append(root)
        
        while queue:
            node = queue.pop(0)
            total+=1
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return total


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

    def print_path(self):
        for stop in self.stops:
            print(stop.get_stop_name())


class PathFinder:
    def __init__(self, avl_tree, metro_lines):
        self.tree = avl_tree
        self.lines = metro_lines

    def get_tree(self):
        return self.tree

    def get_lines(self):
        return self.lines

    def create_avl_tree(self):
        pass  # Implement this method

    def find_path(self, origin, destination):
        trip_prev = None
        trip = Trip(origin, trip_prev)
        
        pass  # Implement this method
   
   
def getfilenames():
    filenames = []
    
    return filenames

def make_metrolines():
    metrolines = []
        
    return metrolines

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        stops = {}
        for line in lines:
            line = line.replace("\n", "")
            line = line.replace(",", "")
            words = line.split()
            stop_name = words[0]
            for word in words[1:-1]:
                stop_name = stop_name + " " + word
            # print(stop_name)
            stop_fare = words[-1]
            # print(stop_fare)
            stops[stop_name] = stop_fare      
        # print(stops)
    return stops
    
    
def read_input():
    filenames = []
    filenames.append("blue.txt")
    filenames.append("green.txt")
    filenames.append("magenta.txt")
    filenames.append("orange.txt")
    filenames.append("red.txt")
    filenames.append("violet.txt")
    filenames.append("yellow.txt")
    
    metrolines = []
    tree = AVLTree()
    for line in filenames:
        metroline = MetroLine()
        metroline.populateLine(line)
        tree.populateTree(metroline)
        metrolines.append(metroline)
    
    pathfinder = PathFinder(tree, metrolines)
    
    
    
    