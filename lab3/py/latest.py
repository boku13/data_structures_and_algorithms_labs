import unittest
import sys
import json

# Import your PhoneBook and PhoneRecord classes here
from lab3 import PhoneBook, PhoneRecord

class CustomTestResult(unittest.TestResult):
    def __init__(self):
        super().__init__()
        self.passed = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.passed.append(test)
        
        # read a .txt file (common for passed and failed) and append the test name to the list
        with open('results_temp.txt', 'a') as f:
            f.write('passed' + ',' + str(test))
            f.write('\n')


    def addFailure(self, test, err):
        super().addFailure(test, err)
        # read a .txt file (common for passed and failed) and append the test name to the list
        with open('results_temp.txt', 'a') as f:
            f.write('failed' + ',' + str(test))
            f.write('\n')
        
    def addError(self, test, err):
        super().addError(test, err)
        # read a .txt file (common for passed and failed) and append the test name to the list
        with open('results_temp.txt', 'a') as f:
            f.write('failed' + ',' + str(test))
            f.write('\n')

class TestPhoneBook(unittest.TestCase):

    # students need to have the functions, (i) create_phone_record and (ii) read records from the file (details.txt) in the
    # phonebook class implemention itself.

    def setUp(self):
        # Create a PhoneBook instance and load data from Details.txt
        self.phone_book = PhoneBook()
        # Students are requested to implement the read_records_from_file() method in your PhoneBook class
        self.phone_book.read_records_from_file("Details_new.txt")

    def test_add_and_fetch_contact(self):
        # Test adding a new contact and then fetching it
        new_contact = PhoneRecord("Adhir Ranjan", "Novotel", ["7889234231"])
        self.phone_book.add_contact(new_contact)
        contacts = self.phone_book.fetch_contacts("Adhir")
        self.assertIn(new_contact, contacts)

    def test_add_and_delete_contact(self):
        # Test adding a new contact and then deleting it
        new_contact = PhoneRecord("Adhir Ranjan", "Novotel", ["7889234231"])
        self.phone_book.add_contact(new_contact)
        self.assertTrue(self.phone_book.delete_contact("Adhir Ranjan"))
        contacts = self.phone_book.fetch_contacts("Adhir Ranjan")
        self.assertNotIn(new_contact, contacts)

    def test_delete_nonexistent_contact(self):
        # Test deleting a contact that doesn't exist (should not delete)
        initial_contacts = self.phone_book.fetch_contacts("Akshay Trivedi")
        print([a.name for a in initial_contacts])
        self.assertFalse(self.phone_book.delete_contact("Akshay Trivedi"))
        contacts_after_delete = self.phone_book.fetch_contacts("Akshay Trivedi")
        self.assertEqual(initial_contacts, contacts_after_delete)

    def test_fetch_nonexistent_contact(self):
        # Test fetching a contact that doesn't exist (should return an empty list)
        contacts = self.phone_book.fetch_contacts("Akshay Trivedi")
        self.assertEqual(len(contacts), 0)

    def test_add_multiple_contacts(self):
        # Test adding multiple contacts with different names

        new_contacts = [PhoneRecord("John", "Benz", ["1111111111"]), PhoneRecord("Atreya", "Tata", ["2222222222"])]
        for contact in new_contacts:
            self.phone_book.add_contact(contact)
        for contact in new_contacts:
            contacts = self.phone_book.fetch_contacts(contact.get_name())
            self.assertIn(contact, contacts)

    def test_delete_multiple_contacts(self):
        # Test deleting multiple contacts with different names
        
        # fetch contacts with the name and store the first contact in the list in a variable
        first_contact_gupta = self.phone_book.fetch_contacts("Ankush Gupta")[0]
        first_contact_khanna = self.phone_book.fetch_contacts("Aarav Khanna")[0]

        self.assertTrue(self.phone_book.delete_contact("Ankush Gupta"))
        self.assertTrue(self.phone_book.delete_contact("Aarav Khanna"))

        # Get the first contact again if any contacts are returned after fetching
        contacts_gupta_after_delete = self.phone_book.fetch_contacts("Ankush Gupta")
        contacts_khanna_after_delete = self.phone_book.fetch_contacts("Aarav Khanna")

        if len(contacts_gupta_after_delete) > 0:
            first_contact_gupta_after_delete = contacts_gupta_after_delete[0]
        # if len(contacts_khanna_after_delete)  0:
        #     first_contact_khanna_after_delete = contacts_khanna_after_delete[0]

        # Check that the first contact after delete (if exists) is not the same as the first contact before deleting
        if len(contacts_gupta_after_delete) > 0:
            self.assertNotEqual(first_contact_gupta, first_contact_gupta_after_delete)

        self.assertNotEqual(0, contacts_khanna_after_delete)

        # Also check that other contacts with the same names are not deleted
        contacts_sharma = self.phone_book.fetch_contacts("Sharma")
        contacts_kumar = self.phone_book.fetch_contacts("Kumar")
        self.assertGreaterEqual(len(contacts_sharma), 1)
        self.assertGreaterEqual(len(contacts_kumar), 1)

    def test_add_delete_fetch_combination(self):
        # Test a combination of add, delete, and fetch operations
        new_contact = PhoneRecord("Venkata Subramanian", "Microsoft", ["8056297058"])
        self.phone_book.add_contact(new_contact)
        self.assertTrue(self.phone_book.delete_contact("Venkata Subramanian"))
        contacts_after_delete = self.phone_book.fetch_contacts("Venkata Subramanian")
        self.assertEqual(len(contacts_after_delete), 0)

    def test_fetch_contacts_with_multiple_words(self):
        # Test fetching contacts with multiple words in the query
        contacts = self.phone_book.fetch_contacts("Kumar")
        self.assertGreaterEqual(len(contacts), 1)

    def test_search_with_middle_name(self):
        # Test searching with a middle name
        contacts = self.phone_book.fetch_contacts("Shekhar")
        self.assertGreaterEqual(len(contacts), 1)

    def test_delete_by_middle_name(self):
        # Test deleting by a middle name
        self.assertTrue(self.phone_book.delete_contact("Dev"))


if __name__ == '__main__':
    # Create a custom test result
    result = CustomTestResult()

    # Run the tests and store the result
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPhoneBook)
    suite(result)

    # print(type(result.passed))

    # Print the number of passed, failed, and error cases
    # print("Passed: {}".format(len(result.passed)))
    # print("Failed: {}".format(len(result.failures)))
    # print("Errors: {}".format(len(result.errors)))

    # create a dict to store the results
    test_results = {}
    test_results["passed"] = len(result.passed)
    test_results["failed"] = len(result.failures) + len(result.errors)


    # print(result.failures)
    # for each in result.passed:
    #     print(each)
    

    test_results['failures'] = str(result.failures)
    # test_results['errors'] = result.errors

    # write the results to a json file
    with open('test_results.json', 'w') as f:
        json.dump(test_results, f)

    # Optionally, you can exit with a non-zero status code if there were failures/errors
    if result.failures or result.errors:
        sys.exit(1)