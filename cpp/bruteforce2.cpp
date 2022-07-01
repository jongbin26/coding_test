#include<iostream>
#include<string>
using namespace std;
int calc(string n) {
	int length = 9 * n.length(), count = 0, solv = 0;
	int num = stoi(n);

	for (int i = num - length; i < num; i++) {
		count += i;
		string str = to_string(i);
		for (int j = 0; j < str.length(); j++) {
			count += (str[j] - '0');
		}
		if (count == num) {
			return i;
		}
		count = 0;
	}

	return 0;
}
int main() {
	string n;
	cin >> n;

	cout << calc(n);
}