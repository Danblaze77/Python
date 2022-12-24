#price of books
b1=int(input("Enter the price of book 1: "))
b2=int(input("Enter the price of book 2: "))
b3=int(input("Enter the price of book 3: "))
b4=int(input("Enter the price of book 4: "))
b5=int(input("Enter the price of book 5: "))
Total=b1+b2+b3+b4+b5
disc=((Total)*(5/100))
amt=Total-disc
print("Discounted amount: ",disc)
print("Amount to be paid: ",amt)
