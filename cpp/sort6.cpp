#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

bool compare(const pair<int, int>& a, const pair<int, int>& b) {
	if (a.first == b.first)
		return a.second < b.second;
	return a.first < b.first;
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, x, y;
	cin >> n;

	vector<pair<int, int>> spot;

	for (int i = 0; i < n; i++) {
		cin >> x >> y;
		spot.push_back({ x,y });
	}

	sort(spot.begin(), spot.end(), compare);

	for (int i = 0; i < n; i++) {
		cout << spot[i].first << " " << spot[i].second<< "\n";
	}

}