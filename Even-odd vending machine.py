

while True:
    num = float(input("Enter a number: "))
    if num.is_integer():
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")
        for x in range(0,21,2):
            print(x+int(num),end=' ')
        break

    else:
        print("Number is not a whole number ")
