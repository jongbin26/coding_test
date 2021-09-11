#include <iostream>
void hanoi(int n, int from, int temp, int to) {
	if (n == 1) {
		printf("%d %d\n", from, to);
		return;
	}
	else {
		hanoi(n - 1, from, to, temp);
		printf("%d %d\n", from, to);
		hanoi(n - 1, temp, from, to);
	}
}
int hanoi_num(int n) {
	if (n == 1) {
		return 1;
	}
	else {
		return 2 * hanoi_num(n - 1) + 1;
	}
}
int main(void) {
	int n;
	int count = 0;
	scanf("%d",&n);
	printf("%d\n",hanoi_num(n));
	hanoi(n, 1, 2, 3);
	return 0;
}