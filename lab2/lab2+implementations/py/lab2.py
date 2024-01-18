EntityArray = []
Students = []

class StudentRecord:
    def __init__(self):
        self.studentName = ""
        self.rollNumber = ""

    def get_studentName(self):
        return self.studentName

    def set_studentName(self, name):
        self.studentName = name

    def get_rollNumber(self):
        return self.rollNumber

    def set_rollNumber(self, rollnum):
        self.rollNumber = rollnum


class Node:
    def __init__(self):
        self.next = None
        self.element = None

    def get_next(self):
        return self.next

    def get_element(self):
        return self.element

    def set_next(self, value):
        self.next = value

    def set_element(self, student):
        self.element = student


class Entity:
    def __init__(self):
        self.name = ""
        self.iterator = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_iterator(self):
        return self.iterator

    def set_iterator(self, iter):
        self.iterator = iter

class LinkedList(Entity):
    def __init__(self):
        super().__init__()
        self.head = None
    
    def add_student(self, student): 
        newnode = Node()
        newnode.element = student
        
        currentnode = self.head
        
        if self.head == None:
            self.head = newnode
            self.iterator = self.head
        
        else: 
            while(currentnode.next):
                currentnode = currentnode.next
                
            currentnode.next = newnode
    
    def delete_student(self, studentname):
        pass
    
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.element.studentName)
            current_node = current_node.next
    

   
def read_input_file(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        details = []
        elements = []
        for line in lines:
            details.append(line.split(','))
        for line in details:
            cleaned_line = []
            for word in line:
                word = word.replace("[", "")
                word = word.replace("]", "")
                word = word.replace("\n", "")
                cleaned_line.append(word)
            elements.append(cleaned_line)
            
    for line in elements:
        student = StudentRecord()
        student.studentName = line[0]
        student.rollNumber = line[1]
        Students.append(student)
        
        entity_made = []
        for entity_name in line[2:]:
            entity = None
            if entity_name not in entity_made:
                entity_made.append(entity_name)
                for i in EntityArray:
                    if i.name == entity_name:
                        entity = i          #storing the reference
                        break
                
                if entity is None:
                    entity = LinkedList()
                    entity.name = entity_name
                    EntityArray.append(entity)
                
            entity.add_student(student)
            
def test3():
    entity_name = "DSA"
    entity = ""
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    ite = entity.get_iterator()
    size = 0
    
    while(ite != None):
        size += 1
        ite = ite.get_next()
    
    print(size)

    assert size == 20, "Incorrect count of records in DSA course"
        
                
            
                
      
read_input_file("Details.txt")
# for entity in EntityArray:
#     print(entity.name)
#     entity.printLL()
test3()



