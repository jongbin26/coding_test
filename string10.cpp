#include<iostream>
#include<string>
using namespace std;
int main() {
	int n;
	int cnt = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		string ward;
		cin >> ward;
		int pos=0, tmp1=0, tmp2 = 0;

		for (int j = 0; j < ward.length(); j++) {
			tmp1 = ward.find(ward[j], pos);
			pos = ward.find(ward[j], pos) + 1;
			tmp2 = ward.find(ward[j], pos);

			if (tmp2 - tmp1 > 1) {
				cnt++;  //cnt=(the number of ungropNum)
				break;
			}
		}
		tmp1 = 0; tmp2 = 0; pos = 0;
	}
	cout << n-cnt;
}