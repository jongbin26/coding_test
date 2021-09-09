#include<iostream>
int fac(int n) {
	if (n == 1 || n==0) {
		return 1;
	}
	return n * fac(n - 1);
}
int main() {
	int n;
	std::cin >> n;
	std::cout << fac(n) << std::endl;
}
//모든 케이스를 포함