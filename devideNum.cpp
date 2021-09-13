#include<iostream>
using namespace std;

int main() {
	int a, b, n, rest, devide;
	cin >> a >> b >> n;

	for (int i = n; i > 0; i--) {
		a %= b;
		a *= 10;
		devide = a / b;
	}

	cout << devide;
}