#suyash raisinghani

year= int(input("Enter year"))

if((year%4==0)and(year%100!=0)or(year%400==0)):
    print("Its a leap year")
else:
    print("It is not a leap year")
