#include <iostream>
using namespace std;

int main() {
    int numYears;
    cout << "Enter number of years: ";
    cin >> numYears;
    double p = 334.23; //initial population
    double B = 12.4/1000;
    double D = 8.4/1000;
    
    for(int i = 2023; i < 2023+numYears; i++) {
        //print current population
        cout << "Year\t" << i << "\t"<< p << endl;
        //calculate next year's expected population
        p = p + B*p - D*p;
    }
}