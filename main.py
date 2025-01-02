def Fibonacci(num):
#two conditions to end the recursion
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
#recursion finding the sum of the two previous numbers
        return Fibonacci(num - 1) + Fibonacci(num - 2)
#loop to print the first 10 numbers of the Fibonacci sequence
print([Fibonacci(i) for i in range(10)],'\n')

nums = []
#first input
inp = input("Enter num: ")
while inp != "stop":
#after each iteration ask the input again and append the num in list
    nums.append(int(inp))
    inp = input("Enter num: ")
print(nums, '\n')