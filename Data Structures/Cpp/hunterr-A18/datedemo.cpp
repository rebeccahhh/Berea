// Filename: DateDemo.cpp
// Example of using the Date class.

#include <iostream>  //Needed for I/O
#include <ctime>  //Needed for the default Date constructor which gets the current date
using namespace std;

//public functions that are used by the class Date
int daysInMonth(int month,int year); 	// # of days in month in year
bool isLeap(int year);   				// is year a leap year

//This is an example of a small C++ class that handles dates
class Date {
  private:
 	//private member variables
    int myDay;                    	// day of week
    int myMonth;                  	// month
    int myYear;                   	// year in four digits, e.g., 2003

    //private member function
    void checkDate(int m, int d, int y); 	// make sure that date is valid

  public:
    // constructors
    Date();                       	// construct date with default value
    Date(int m,int d,int y);      	// construct date with specified values

    // public member functions called accessors since they are used
    // to access the contents of private member variables
    int getMonth()	const;     // return month corresponding to date
    int getDay()	const;     // return day corresponding to date
    int getYear()	const;     // return year corresponding to date
    
    //public member function
    void print()	const; //Will cout a date in the 1/1/2003 format
    void store()    const;

}; // Note the need for a semicolon just like ending a structure

int main() {
    // This calls the default Date constructor, which sets the current date.
    Date todaydate;
    cout << "Today is ";
    todaydate.print();
    cout << "." << endl;

    int userdate;
    int userint;
    cout << "Please enter a date (1-12): ";
    cin >> userdate;
    cout << "Please enter an integer(1-100): ";
    cin >> userint;

	int birthmonth, birthday, birthyear;
    cout << "Please enter the month (1-12) you were born: ";
    cin >> birthmonth;
    cout << "Please enter the date (1-31) of your birthday: ";
    cin >> birthday;
    cout << "Please enter the year you were born: ";
    cin >> birthyear;

    //This calls the Date contructor and sets the member variables of birthdate.
    Date birthdate(birthmonth, birthday, birthyear);

    cout << "You were born ";
    birthdate.print();
    cout << "." << endl;

    //Note that we cannot use birthdate.myMonth here since myMonth is a private member variable
    if (birthdate.getMonth() == todaydate.getMonth()) {
    	//cout << birthdate.myMonth; //Uncomment this to see what happens
    	cout << "Hey, you have a birthday this month!" << endl;
    }
    else {
    	cout << "Too bad you don't have a birthday this month..." << endl;
    }
    return 0;
} //end main


bool isLeap(int year) {
// postcondition: returns true if year is a leap year, else returns false

    if (year % 400 == 0) {
        return true;
    }
    else if (year % 100 == 0) {
        return false;
    }
    else if (year % 4 == 0) {
        return true;
    }
    return false;
}

int daysInMonth(int month, int year) {
// postcondition: returns # of days in month in year

    // Start with 31 days and lower it to 30 for April, June, September
    // and November. Then handle February.
    int days = 31;

    if( month == 4 || month == 6 || month == 9 || month == 11 ) {
        days = 30;
   	}
    else if (month == 2) {          // handle February
        days = 28;
        if (isLeap(year)) {        // add 1 for leap years
            days += 1;
       	}
    }
    return days;
}

Date::Date()
//Do not worry about understanding the contents of this constructor yet.
//Getting the current date uses ideas we have not yet learned...
// postcondition: date initialized to default date of today
{
    static struct tm timeHolder;
    static struct tm *date = &timeHolder;
    time_t tloc;

    time(&tloc);

    date = localtime(&tloc);

    myMonth = date->tm_mon + 1;
    myDay   = date->tm_mday;
    myYear  = date->tm_year + 1900;             // struct tm based on 1900
}

Date::Date(int m, int d, int y) {
// postcondition: date properly initialized for date m/d/y
// exception:  if m isn't between 1 and 12, converted to 1
//             if d out of range for month, converted to 1
//			   if year is 2 digits, 1900 is added
    checkDate(m,d,y);
}


int Date::getMonth() const {
// postcondition: returns month of Date
    return myMonth;
}

int Date::getDay() const {
// postcondition: returns day of Date
    return myDay;
}

int Date::getYear() const {
// postcondition: returns year of Date
    return myYear;
}

void Date::print() const {
//postcondition: cout a date in the 1/1/2003 format
    cout << myMonth << "/" << myDay << "/" << myYear;
}


void Date::store() const {
//postcondition: takes as input a number of days and adds that to a Date object
}

void Date::checkDate( int m, int d, int y ) {
// postcondition: adjusts out-of-range dates before setting member variables
    if (m < 1 || 12 < m) {               // If the month is out of range, set it to January
    	m = 1;
    	cout << "WARNING: Invalid month set to January." << endl;
    }
    myMonth = m;

    if (d < 1 || daysInMonth(m,y) < d) { // If the day is out of range, set it to 1.
    	d = 1;
    	cout << "WARNING: Invalid day set to 1." << endl;
    }
    myDay = d;

    if (y < 100) {                       // If the year is given in 2 digits, add 1900.
    	y = y + 1900;
    }
    myYear = y;
}

