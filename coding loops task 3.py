n = int(input("Enter the number of terms: "))
num1, num2 = 0, 1
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence upto", n, "term:")
    print(num1)
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(num1)
        next_num = num1 + num2
        num1 = num2
        num2 = next_num

OUTPUT

Enter the number of terms: 10
Fibonacci sequence:
0
1
1
2
3
5
8
13
21
34

