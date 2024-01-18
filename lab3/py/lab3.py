from collections import Counter
class PhoneRecord:
    def __init__(self, name, organisation, phone_numbers):
        self.name = name
        self.organisation = organisation
        self.phone_numbers = phone_numbers

    def get_name(self):
        return self.name

    def get_organisation(self):
        return self.organisation

    def get_phone_numbers(self):
        return self.phone_numbers


class HashTableRecord:
    def __init__(self, key, record):
        self.key = key
        self.record = record    #element
        self.next = None

    def get_key(self):
        return self.key

    def get_record(self):
        return self.record  

    def get_next(self):
        return self.next

    def set_next(self, nxt):
        self.next = nxt


class PhoneBook:
    HASH_TABLE_SIZE = 263

    def __init__(self):
        self.hash_table = [None] * PhoneBook.HASH_TABLE_SIZE

    def compute_hash(self, string):
        term = 0
        x = 1
        calc = 0
        p = 10e9 + 7
        count = 0 

        for i in string:
            ascii = ord(i)
            term = ascii*x
            x = x*263
            term = term%p
            calc +=term
            # print(count, ":", calc)
            count+=1
                
        m = 263
        calc = calc%m
        return int(calc)

    def add_contact(self, record):
        #Implement adding a contact to the phone book
        #You need to compute the hash for the record's name and insert it into the hash table
        names = record.name.split()
        
        for name in names:
            #print(name)
            key = self.compute_hash(name)
            #print(key)
            ht_record = HashTableRecord(key, record)
            head = self.hash_table[key]
            ht_record.next = head
            self.hash_table[key] = ht_record
            
            # if head is None:
            #     self.hash_table[key] = ht_record
            # else:
            #     while head.next is not None:
            #         head = head.next 
            #     head.next = ht_record

    def delete_contact(self, name):
    #     # Implement deleting a contact from the phone book
    #     # You need to find the record with the given name and remove it from the hash table
        contact_list = self.fetch_contacts(name)
        if len(contact_list) == 0:
            return False
        else:
            contact = contact_list[0]
        
        names = name.split()
        # nothing_deleted = 0
        deleted = 0
        for word in names:
            key = self.compute_hash(word)
            head = self.hash_table[key]
            prev = None
            # print(head.record.name)
            if head is not None:
                while head is not None:
                    if(head.record == contact): 
                        if prev is None:
                            self.hash_table[key] = head.next
                        else:
                            prev.next = head.next
                        deleted += 1
                    prev = head 
                    head = head.next 
            # else:
            #     nothing_deleted+=1
        if deleted > 0:
            return True
        else:
            return False            

    def fetch_contacts(self, query):
        # Implement fetching contacts based on the query
        # You may need to split the query into words and hash them separately
        # Then, retrieve and merge the records from the appropriate hash table slots
        # Sort and return the merged records
        result = []
        names = query.split()
        for name in names: 
            key = self.compute_hash(name)
            head = self.hash_table[key]
            while head is not None:
                result.append(head.record)
                head = head.next
        # # print(result)
        # for results in result:
        #     print(results.name)
        sorted_result = [item for items, c in Counter(result).most_common()
                                      for item in [items] * c]
        # print(sorted_result)
        return sorted_result
    
    def create_phone_record(self, contact_info):
        row = contact_info.split(",")
        name = row.pop(0)
        org = row.pop()
        #return row
        record = PhoneRecord(name, org, row)
        
        return record  
        
    def read_records_from_file(self, file_path):
        with open(file_path) as f:
            lines = f.readlines()
            details = []
            elements = []
            for line in lines:
                line = line.replace("\n", "")
                details.append(line)
            # print(details)    
            # for line in details:
            #     cleaned_line = []
            #     for word in line:
            #         # word = word.replace("[", "")
            #         # word = word.replace("]", "")
            #         word = word.replace("\n", "")
            #         cleaned_line.append(word)
            #     elements.append(cleaned_line) 
            # print(elements) 
            
        for contact_info in details:
            record = self.create_phone_record(contact_info) 
            self.add_contact(record)
                
        # for row in elements:
        #     name = row.pop(0)
        #     org = row.pop()
        #     #return row
        #     record = PhoneRecord(name, org, row)
        #     self.add_contact(record)       
                # make multiple records for different phone numbers? no, pass them as a list/tuple
                
    def print_hash_table(self):
        for index, linked_list in enumerate(self.hash_table):
            print(f"Index {index}:")
            current = linked_list
            while current is not None:
                print(f"   {current.record}")  # Assuming each record has a __str__ method
                current = current.next
    
# def read_input_file(file_path):
#     # with open(file_path) as f:
#     #     lines = f.readlines()
#     #     details = []
#     #     elements = []
#     #     for line in lines:
#     #         details.append(line.split(','))
#     #     for line in details:
#     #         cleaned_line = []
#     #         for word in line:
#     #             # word = word.replace("[", "")
#     #             # word = word.replace("]", "")
#     #             word = word.replace("\n", "")
#     #             cleaned_line.append(word)
#     #         elements.append(cleaned_line)
            
#     phonebook = PhoneBook()     
    
#     # count = 0
#     # for row in elements:
#     #     names = row[0].split()
#     #     print(names)
#     #     for name in names:
#     #         count+=1
#     # print(count)
        
#     for row in elements:
#         name = row.pop(0)
#         org = row.pop()
#         #return row
#         record = PhoneRecord(name, org, row)
#         phonebook.add_contact(record)       
#             # make multiple records for different phone numbers? no, pass them as a list/tuple
    
#     results = phonebook.fetch_contacts("Rahul Kumar Mishra")
#     print(results)
#     for result in results:
#         print(result.name)
    
            
    # key1 = phonebook.compute_hash("Rahul")
    # print(key1)
    # key2 = phonebook.compute_hash("Kumar")
    # print(key2)
    # key3 = phonebook.compute_hash("Mishra")
    # print(key3)
    
    # print(phonebook.hash_table[key1].record.name)
    # print(phonebook.hash_table[key2].record.name)
    # print(phonebook.hash_table[key3].record.name)
    
    # count = 0
    # for i in phonebook.hash_table:
    #     # if i is not None:
    #         # count +=1
    #         # print(count)
    #         # print(i.key)
    #         # print(i.record.name)
    #     head = i
    #     if i is not None:
    #         while head is not None:
    #             count+=1
    #             print(count)
    #             print(head.key)
    #             print(head.record.name)
    #             head = head.next
    
    #return elements
    

phonebook = PhoneBook()
phonebook.read_records_from_file("Details.txt")
# # fc_check1 = phonebook.fetch_contacts("Ritu Kumar")
# # fc_check2 = phonebook.fetch_contacts("Priya Das")

# # for records in fc_check2:
# #     print(records.name)
    
# # for records in fc_check1:
# #     print(records.name)
# phonebook.print_hash_table()

# new_contact_info = "John Doe,1234567890,Company ABC"
# new_contact = phonebook.create_phone_record(new_contact_info)
# phonebook.add_contact(new_contact)
# phonebook.print_hash_table()
# contacts = phonebook.fetch_contacts("John Doe")
# print(contacts)
# phonebook.delete_contact("John Doe")
# phonebook.print_hash_table()

# new_contact_info = "New Contact,9999999999,Test Company"
# new_contact = phonebook.create_phone_record(new_contact_info)
# phonebook.add_contact(new_contact)
# contacts_before_delete = phonebook.fetch_contacts("New Contact")
# print(contacts_before_delete)
# phonebook.print_hash_table()
# phonebook.delete_contact("New Contact")
# contacts_after_delete = phonebook.fetch_contacts("New Contact")
# print(contacts_after_delete)
# phonebook.print_hash_table()

# print(phonebook.compute_hash("New"))
# print(phonebook.compute_hash("Contact"))