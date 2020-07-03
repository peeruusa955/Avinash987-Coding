/*Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines.
First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

Output:
For each test case, print the count of all triplets, in new line. If no such triplets can form, print "-1". */
#include<iostream>
#include<algorithm> // std::sort
using namespace std;

//Logic
void CountTriplets(int array[], int N)
{
    int count = 0;
    if(N <= 2)
        cout<< -1 <<endl;

    sort(array, array+N);

    for (int i = N - 1; i >= 0; i--)
    {
        int j = 0;
        int k = i - 1;

        while (j < k)
        {
            if (array[i] == array[j] + array[k])
                count += 1;
            else if (array[i] > array[j] + array[k])
                j += 1;
            else
                k -= 1;
        }
    }
    if(count == 0)
        count = -1;

    cout<< count <<endl;
    return;
}

int main(void)
{
    int T, N;
    cin >> T;
    // For all the test cases
    for(int t=0; t<T; t++)
    {
        cin >> N;
        int array[N];
        // Take the array input rrom the user
        for(int i=0; i<N; i++)
            cin >> array[i];

        CountTriplets(array, N);

    }
    return 0;
}