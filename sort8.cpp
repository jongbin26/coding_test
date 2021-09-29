#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

bool compare(string s1, string s2) {
	if (s1.length() == s2.length())
		return s1 < s2;
	return s1.length() < s2.length();
}

int main() {
	int n;
	string input;
	cin >> n;

	vector <string> str;
	string temp;

	for (int i = 0; i < n; i++) {
		cin >> input;
		if (find(str.begin(), str.end(), input) == str.end())
			str.push_back(input);
	}

	for (int i = 0; i < str.size(); i++) {
		for (int j = i + 1; j < str.size(); j++) {
			if (str[i].length() > str[j].length()) {
				temp = str[i];
				str[i] = str[j];
				str[j] = temp;
			}
		}
	}

	sort(str.begin(), str.end(), compare);

	for (int i = 0; i < str.size(); i++) {
		cout << str[i] << "\n";
	}
}