#include <iostream>
using namespace std;

int main() {
	int time;
	do {
		cout << "Enter time in 24 hour format: ";
		cin >> time;		
	} while (time < 0 || time > 2400);

	if (time < 1200) {
		cout << "Morning";
	} else if (time > 1800) {
		cout << "Evening";
	} else {
		cout << "Afternoon";
	}

	cout << "\n";
}