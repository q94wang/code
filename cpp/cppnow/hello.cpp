// The MIT License (MIT)

// Copyright (c) 2019 C++Now

//  Permission is hereby granted, free of charge, to any person obtaining a
//  copy of this software and associated documentation files (the "Software"),
//  to deal in the Software without restriction, including without limitation
//  the rights to use, copy, modify, merge, publish, distribute, sublicense,
//  and/or sell copies of the Software, and to permit persons to whom the
//  Software is furnished to do so, subject to the following conditions:
//
//  The above copyright notice and this permission notice shall be included in
//  all copies or substantial portions of the Software.
//
//  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
//  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
//  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
//  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
//  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
//  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
//  DEALINGS IN THE SOFTWARE.

/* code */


#include <iostream>
using namespace std;


class Calculator
{
private:
    /* data */
public:
    Calculator(/* args */) { }
    ~Calculator() { }
    void PrimeGenerator(int, int);
};


int main(int argc, char const *argv[])
{
    /* code */
    cout << "Please enter two numbers: " << endl;
    int x, y;
    cin >> x >> y;
    Calculator c;
    c.PrimeGenerator(x, y);

    cin.ignore();
    cin.get();

    return 0;
}

void Calculator::PrimeGenerator(int x, int y)
{
    for (int i = x; i < y; i++)
    {
        /* code */
        bool prime = true;
        for (int j = 2; j * j <= i; j++)
        {
            if (i % j == 0)
            {
                prime = false;
                break;
            }
        }

        if (prime == true)
        {
            cout << i << " ";
        }
    }
}