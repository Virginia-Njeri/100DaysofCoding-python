amt=0
number=int(input("enter your unit"))
if number<=100:
    amt=0
if number>100 and number<=200:
    amt=(number-100)*5
if number>=200:
    amt=500+(number-200)*10
    print("Amount to pay :",amt)