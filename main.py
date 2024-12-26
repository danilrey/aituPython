codes = {
    'A' : '%','a' : '9',
    'B' : '!','b' : '8',
    'C' : '@','c' : '7',
    'D' : '#','d' : '6',
    'E' : '$','e' : '5',
    'F' : '^','f' : '4',
    'G' : '&','g' : '3',
    'H' : '*','h' : '2',
    'I' : '(','i' : '1',
    'J' : ')','j' : '0',
    'K' : '_','k' : '-',
    'L' : '+','l' : '=',
    'M' : '[','m' : '{',
    'N' : ']','n' : '}',
    'O' : ';','o' : ':',
    'P' : "'",'p' : '"',
    'Q' : ',','q' : '<',
    'R' : '.','r' : '>',
    'S' : '/','s' : '?',
    'T' : '|','t' : '\\',
    'U' : '`','u' : '~',
    'V' : '!','v' : '@',
    'W' : '#','w' : '$',
    'X' : '%','x' : '^',
    'Y' : '&','y' : '*',
    'Z' : '(','z' : ')',
}

usIn = input("Enter a string: ")
usIn = list(usIn)
for i in range(len(usIn)):
    if usIn[i] in codes:
        usIn[i] = codes[usIn[i]]
    else:
        usIn[i] = usIn[i]
print("".join(usIn))