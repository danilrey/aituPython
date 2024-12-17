a = int(input("Enter the num of packages"))
discount = 1

if a >= 10 and a <= 19:
    print("Your discount is 20%")
    discount = 0.2
elif a >= 20 and a <= 49:
    print('Your discount is 30%')
    discount = 0.3
elif a >= 50 and a <= 99:
    print('Your discount is 40%')
    discount = 0.4
elif a >= 100:
    print('Your discount is 50%')
    discount = 0.5
else:
    print('There is no discount for you')

print(a*99*discount)