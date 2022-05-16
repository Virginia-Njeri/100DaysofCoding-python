while True:
    price=int(input("Enter the bike price:"))
    if price > 100000:
       tax=15/100*price
    elif price> 50000 and price <= 100000:
         tax=10/100*price 
    else: price<= 50000   
    tax=5/100*price
    print("Tax to be paid",tax)