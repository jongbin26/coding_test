#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, k;
	cin >> n;

	int cnt = 0;

	vector<int> x;
	vector<int> temp;

	for (int i = 0; i < n; i++) {
		cin >> k;
		x.push_back(k);
		temp.push_back(k);
	}

	temp = x;
	sort(temp.begin(), temp.end());
	temp.erase(unique(temp.begin(), temp.end()), temp.end());

	for (int i : x) {
		int pos = lower_bound(temp.begin(), temp.end(), i) - temp.begin();
		cout << pos << " ";
	}
}


//#include<iostream>
//#include<algorithm>
//#include<vector>
//using namespace std;
//int main() {
//	ios::sync_with_stdio(false);
//	cin.tie(NULL);
//	cout.tie(NULL);
//
//	int n, k;
//	cin >> n;
//
//	int cnt = 0;
//
//	vector<int> x;
//	vector<int> temp;
//
//	for (int i = 0; i < n; i++) {
//		cin >> k;
//		x.push_back(k);
//		temp.push_back(k);
//	}
//
//	temp = x;
//	sort(temp.begin(), temp.end());
//	temp.erase(unique(temp.begin(), temp.end()), temp.end());
//
//	for (int i : x) {
//		int pos = lower_bound(temp.begin(), temp.end(), i) - temp.begin();
//		cout << pos << " ";
//	}
//}