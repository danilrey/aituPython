a = int(input("Number of days: "))
money = []
result = []

for i in range(a):
    money.append(int(input(f"Enter number of money in {i+1} day: ")))

def check_for_buying(num):
    if num < 7:
        return -1
    powers = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    copynum = num
    sumRes = 0
    count = 0
    while copynum >= 1 and count < 3:
        if copynum in powers and (sumRes + copynum) <= num:
            sumRes += copynum
            powers.remove(copynum)
            count += 1
        copynum -= 1
    if count != 3:
        return -1
    else:
        return sumRes

for i in range(a):
    result.append(check_for_buying(money[i]))
    print(result[i])
