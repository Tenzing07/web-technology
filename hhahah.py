num = int(input("enter the number:"))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")
else:
    print("it is not a prime number")    