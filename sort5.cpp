#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

bool compare(int i, int j) {
	return j < i;
}
int main() {
	string n;
	cin >> n;
	sort(n.begin(), n.end(), compare);

	cout << n;
}