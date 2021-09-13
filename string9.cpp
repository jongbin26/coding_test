#include<iostream>
#include<string>
using namespace std;

int main() {
	string alp[8] = { "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=" };
	string input;
	cin >> input;
	int idx;
	
	for (int i = 0; i < 8; i++) {
		while (true) {
			idx = input.find(alp[i]);
			if (idx == string::npos)
				break;

			input.replace(idx, alp[i].length(), "*");
		}
	}

	cout << input.length();
}