#include<iostream>
#include<queue>
#include<cmath>
#include<algorithm>
using namespace std;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, total = 0;
	cin >> n;
	int* arr = new int[n]();
	int cnt[8001] = {};

	//배열 입력
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		total += arr[i];
	}

	//산술평균
	cout << round((float)total / n) << "\n";

	//중앙값
	sort(arr, arr + n);
	cout << arr[n / 2] << "\n";

	//최빈값
	int max = 0;

	for (int i = 0; i < n; i++) {
		cnt[arr[i] + 4000]++;
		if (cnt[arr[i] + 4000] > max)
			max = cnt[arr[i] + 4000];
	}

	queue<int> most;

	for (int i = -4000; i <= 4000; i++) {
		if (cnt[i + 4000] == max)
			most.push(i);
	}

	if (most.size() > 1) {
		most.pop();
		cout << most.front() << "\n";
	}
	 else {
		cout << most.front() << "\n";
	}
	 
	
	//범위
	cout << arr[n - 1] - arr[0] << "\n";
}