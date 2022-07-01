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

	//�迭 �Է�
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		total += arr[i];
	}

	//������
	cout << round((float)total / n) << "\n";

	//�߾Ӱ�
	sort(arr, arr + n);
	cout << arr[n / 2] << "\n";

	//�ֺ�
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
	 
	
	//����
	cout << arr[n - 1] - arr[0] << "\n";
}