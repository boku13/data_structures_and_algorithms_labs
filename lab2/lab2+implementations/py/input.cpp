#include <iostream>
#include <sstream>
#include <vector>
#include <fstream>
#include <string>


using namespace std;

class Details {
private:
    //member variable
    std::string Name;
    std::string Roll_No;
    std::string Department;
    std::string Course;
    std::string Hostel;
    std::string Club;

public:

    //overload constructor
    Details(const std::string& Details)
    {
        std::istringstream DetailsStream(Details);
        std::getline(DetailsStream, Name, ',');
        std::getline(DetailsStream, Roll_No, ',');
        std::getline(DetailsStream, Department, ',');
        std::getline(DetailsStream, Course, ',');
        std::getline(DetailsStream, Hostel, ',');
        std::getline(DetailsStream, Club, ',');
    }
    //Access methods
    std::string getName() const { return Name; };
    std::string getRollNo()  const { return Roll_No; };
    std::string getDepartment()  const { return Department; };
    std::string getCourse()  const { return Course; };
    std::string getHostel()  const { return Hostel; };
    std::string getClub()  const { return Club; };

    //Destructor
    ~Details() {};
};

int main(){
    std::ifstream ifs{ "Details.txt" };
    if (ifs) {

        // Here we will store all details
        std::vector<Details> details{};

        // Read the file line by line
        std::string line{};
        while (std::getline(ifs, line)) {

            // Create one detail by splitting the input line
            Details detail(line);

            // Add the new details to the vector of details
            details.push_back(detail);
        }

        // Debug output. For all details that we read, output all data
        for (const Details& detail : details) {

            std::cout << "\n--------------------------\n"
             << detail.getName() << '\n'
             << detail.getRollNo() << '\n'
             << detail.getDepartment() << '\n'
             << detail.getCourse() << '\n'
             << detail.getHostel() << '\n'
             << detail.getClub() << '\n';
        }
    }
    else{
        std::cerr << "\n*** Error: Could not open source file\n\n";
    }

     return 0;
}