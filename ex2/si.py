#simple interest
P=int(input("Enter the principal amount: "))
t=int(input("Enter time period for months: "))
r=int(input("Enter the rate of interest: "))
SI=(P*t*r)/100
A=P+SI
print("Simple interest "+str(SI))
print("Amount: "+str(A))
