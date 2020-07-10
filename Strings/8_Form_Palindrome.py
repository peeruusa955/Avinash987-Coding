"""
Given a string, find the minimum number of characters to be inserted
to convert it to palindrome.
For Example:
ab: Number of insertions required is 1. bab or aba
aa: Number of insertions required is 0. aa
abcd: Number of insertions required is 3. dcbabcd
"""

def check_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

def toFormPalindrome(s):



if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        string = str(input())
        result = toFormPalindrome(string)
        print(result)