# Pattern problem from hackerrank
# Remember the sample logic
# num = 9

# for i in range(1, num+1):
#   i = i - (num//2 +1)
#   if i < 0:
#     i = -i
#   print(" " * i + "*" * (num - i*2) + " "*i)


def print_rangoli(size):
    # your code goes here
    length, height = (2*size-1)+(2*size-2), 2*size-1

    char = [chr(digit) for digit in  range(97, 97+size)]
    print(char)
    for i in range(1, height+1):

        char_list = []
        index_list = []
        mid = height//2 + 1
        if i <= mid:
            char_len = 2*i-1
            for j in range(1, char_len+1):
                if j <= char_len//2 + 1:
                    char_list.append(char[-j])
                    index_list.append(-j)
                else:
                    char_list.append(char[-(char_len + 1) + j])
                    index_list.append(-(char_len + 1) + j)
            # print(char_list)
            # print(index_list)
            listoStr = '-'.join(char_list)
            print(listoStr.center(length, '-'))
        else:
            char_len = height - (i - mid)*2
            for j in range(1, char_len+1):
                if j <= char_len//2 + 1:
                    char_list.append(char[-j])
                    index_list.append(-j)
                else:
                    char_list.append(char[-(char_len + 1) + j])
                    index_list.append(-(char_len + 1) + j)
            # print(char_list)
            # print(index_list)
            listoStr = '-'.join(char_list)
            print(listoStr.center(length, '-'))



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)