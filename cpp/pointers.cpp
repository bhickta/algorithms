#include<iostream>
using namespace std;
int main() {
    int a = 33;
    int b = 55;
    int *ptr = &a;
    ptr = &b;
    cout << *ptr << endl;
    cout << sizeof(ptr) << endl << sizeof(*ptr) << endl;

    int arr[4] = {1, 3, 4};
    cout << arr[0] + 11 << endl;
    cout << *(arr) << endl;
}

// https://youtu.be/KA3XnH6eYpY?list=PLQEaRBV9gAFttZ9ArI8oMp8eVrBC8ey-Y