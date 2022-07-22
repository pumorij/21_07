# input number between 1200 to 3000 print number divisible by 8 and 4 but not 6


num=int(input("Input number between 1200 to 3000: "))


if(num>=1200 and num<=3000):
    if((num%8==0)and (num%4==0) and (num%6!=0) ):
        print("YES")
    else:
        print("NO")