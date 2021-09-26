#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, k;
	cin >> n;

	int arr[10001] = {};
	for (int i = 0; i < n; i++) {
		cin >> k;
		arr[k]++;
	}

	for (int i = 1; i <= 10000; i++) {
		for (int j = 0; j < arr[i]; j++)
			cout << i << "\n";
	}
}