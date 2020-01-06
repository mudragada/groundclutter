#include <iostream>
using namespace std;
 
int main () {
	int locker = 54;
	int *safe = &locker;
	int **bank = &safe;
	int ***area = &bank;
	int ****city = &area;

	cout << "value of locker: locker= " << locker << endl;
	cout << "value at address of locker: *&locker= " << *(&locker) << endl;
	cout << "value at locker's address: *safe= " << *safe << endl;
	cout << "address of locker(safe): &locker= " << &locker << endl;
	cout << "address of locker(safe): safe= " << safe << endl;
	cout << "address of safe(bank): bank= " << bank << endl;
	cout << "address of bank(area): &bank= " << &bank << endl;
	cout << "address of bank(area): area= " << area << endl;
	cout << "address of area(city): &area= " << &area << endl;
	cout << "address of area(city): city= " << city << endl;
	cout << "address of city: &city= " << &city << endl;
}