#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

struct Member
{
	int age;
	string name;
	int num;
};

bool compare(Member a, Member b) {
	if (a.age < b.age)
		return true;
	else if (a.age == b.age)
		return a.num < b.num;
	else
		return false;
}

int main() {
	int n;
	cin >> n;

	vector<Member> member(n);

	for (int i = 0; i < n; i++) {
		cin >> member[i].age >> member[i].name;
		member[i].num = i;
	}

	sort(member.begin(), member.end(), compare);

	for (int i = 0; i < member.size(); i++) {
		cout << member[i].age << " " << member[i].name << "\n";
	}
}