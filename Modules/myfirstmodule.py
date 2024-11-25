def palindrome():
    word = input("Enter a word:")
    str_rev=word[::-1]
    if str_rev==word:
        print(f"The word \"{word}\" is a palindrome")
    else:
        print(f"The word \"{word}\" is not a palindrome")

def prime_check():
    n = int(input("Enter the number: "))
    cnt=0
    if n<=1:
        print(f"{n} is not a prime number")
    else:
        for i in range(2,n+1):
            if n%i == 0:
                cnt = cnt + 1          
        if cnt>=2:
            print(f"{n} is NOT a prime number")  
        else:
            print(f"{n} is a prime number")
