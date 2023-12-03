#include <iostream>
using namespace std;
int main() {
    for (int a, i = 2; i * i <= (cin >> a, a); i++) {
        if (a % i == 0) {
            cout << "Not prime";
            return 0;
        }
    }

    cout << "Is prime";
    return 0;
}