num = int(input("Enter the maximum number of star: "))

for i in range(num):
    for j in range(i+1):
        print("*",end='')
    print()