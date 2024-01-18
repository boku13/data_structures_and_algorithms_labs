import sys
from interface_template import StudentRecord
from interface_template import EntityArray 
from interface_template import LinkedList
from interface_template import read_input_file

failed_tests = 0

def test1():
    entity_name = "CSE"
    entity = ""
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    ite = entity.get_iterator()
    student = ""
    
    while(ite != None):
        if ite.get_element().studentName == "JohnDoe":
            student = ite.get_element()
            break
        ite = ite.get_next()

    assert student.studentName == "JohnDoe", "Student JohnDoe is not present in the CSE Entity"

def test2():
    entity_name = "EE"
    entity = ""
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    ite = entity.get_iterator()
    student = ""
    
    while(ite != None):
        if ite.get_element().studentName == "SanyaSharma":
            student = ite.get_element()
            break
        ite = ite.get_next()

    assert student.studentName == "SanyaSharma", "Student SanyaSharma is not present in the EE Entity"

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

    assert size == 20, "Incorrect count of records in DSA course"

def test4():
    entity_name = "Programming"
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

    assert size == 20, "Incorrect count of records in Programming Club"

def test5():
    entity_name = "Toastmasters"
    entity = ""
    studentname = "RaviKumar"
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    entity.delete_student(studentname)
    ite = entity.get_iterator()
    
    if_exists = 0
    while(ite != None):
        if ite.get_element().studentName == studentname:
            if_exists = 1
            break
        ite = ite.get_next()

    assert if_exists == 0, "Record still exists, Delete function not working!"

def test6():
    entity_name = "Maths"
    entity = ""
    studentname = "UzumakiNaruto"
    studentroll = "B20CS011"
    student = StudentRecord()
    student.studentName = studentname
    student.rollNumber = studentroll

    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    entity.add_student(student)
    ite = entity.get_iterator()
    
    if_exists = 0
    while(ite != None):
        if ite.get_element().studentName == studentname:
            if_exists = 1
            break
        ite = ite.get_next()

    assert if_exists == 1, "Record is not added, Add Student Record function not working!"

def test7():
    entity_name = "PRML"
    entity = ""
    studentname = "HimashuGupta"
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    entity.delete_student(studentname)
    ite = entity.get_iterator()
    
    if_exists = 0
    while(ite != None):
        if ite.get_element().studentName == studentname:
            if_exists = 1
            break
        ite = ite.get_next()

    assert if_exists == 0, "Record still exists, Delete function not working!"

def test8():
    entity_name = "G5"
    entity = ""
    studentname = "UchihaSasuke"
    studentroll = "B20ES011"
    student = StudentRecord()
    student.studentName = studentname
    student.rollNumber = studentroll

    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    entity.add_student(student)
    ite = entity.get_iterator()
    
    if_exists = 0
    while(ite != None):
        if ite.get_element().studentName == studentname:
            if_exists = 1
            break
        ite = ite.get_next()

    assert if_exists == 1, "Record is not added, Add Student Record function not working!"

if __name__ == "__main__":
    
    unit_tests_list = [
        test1, test2, test3, test4, test5, test6,
        test7, test8
    ]
    total = len(unit_tests_list)
    try:
        read_input_file("Details.txt")
    except:
        print("Could not read Sample Input File! Ensure that the file 'details.txt' is in the folder and try again!")
        sys.exit(1)
        
    for i, test_fn in enumerate(unit_tests_list):
        try:
            test_fn()
        except Exception as e:
            failed_tests += 1
            print(f"Unit test #{i+1} failure: {str(e)}")

    if failed_tests == 0:
        print("All tests have passed successfully!")
    else:
        print(f"{failed_tests} tests failed!")
    sys.exit(failed_tests)
