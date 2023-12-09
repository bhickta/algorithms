#include <iostream>
using namespace std;

void row_col_nums()
{
    int n;
    cout << "Enter a Number\n";
    cin >> n;
    char counting = 'A';
    int i = 0; /* i = n => inverted-triangle*/
    while (i < n)
    {
        int j = 0;
        while (j <= i) /* j < i + 1 = upright-triangle pattern | j < n = square pattern */
        {
            cout << counting; /* j+1 = front col | i + 1 = front row | n - i reverse rows | "*" row-col equal stars | counting++ = counting | i + 1 - j = reverse rows*/
            counting++;
            j++;
        }
        cout << endl;
        i++; /* i-- inverted-triangle*/
    }
}

int main()
{
    row_col_nums();
}