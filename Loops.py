Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

Example

The list of non-negative integers that are less than 3 is 0,1,2 . Print the square of each number on a separate line.

if __name__ == '__main__':
    n = int(input())
    num = 0
    while num < n:
        print(num*num)
        num += 1
