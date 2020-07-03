/*Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines.
First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

Output:
For each test case, print the count of all triplets, in new line. If no such triplets can form, print "-1". */

int main(void)
{
    int T, N, S;
    cin >> T;
    // For all the test cases
    for(int t=0; t<T; t++)
    {
        cin >> N >> S;
        int array[N];
        // Take the array input rrom the user
        for(int i=0; i<N; i++)
            cin >> array[i];

        // SubArraySum(array, N, S);

    }
    return 0;
}