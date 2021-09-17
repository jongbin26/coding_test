#include<iostream>
#include<vector>
using namespace std;

int main() {
	int n, m;
	cin >> n >> m;
	int* num = new int[n]();
	int err=300000, err2 = 300000;
	int solution=0;

	for (int i = 0;i < n; i++) {
		cin >> num[i];
	}

	for (int i = 0; i < n-2; i++) {
		for (int j = i+1; j < n-1; j++) {
			for (int k = j+1; k < n; k++) {
				if ((m - (num[i] + num[j] + num[k])) >= 0) {
					if ((m - (num[i] + num[j] + num[k])) < err) {
						err = (m - (num[i] + num[j] + num[k]));
					}
				}
			}
		}
	}
	
	solution = m - err;
	std::cout << solution;
	delete[] num;
	return 0;
}