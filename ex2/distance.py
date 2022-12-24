#distanc ebetween two poitns
x1=int(input("Enter the co-ordinates of x1"))
x2=int(input("Enter the co-ordinates of x2"))
y1=int(input("Enter the co-ordinates of y1"))
y2=int(input("Enter the co-ordinates of y2"))
distance=(((x2-x1)**2)+((y2-y1)**2))**(1/2)
print("The distance between two given points are: "+str(distance))
