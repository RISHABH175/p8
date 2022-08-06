p=int(input("Enter the prime number p:  "))
alpha=int(input("Enter the alpha:   "))

a=int(input("Enter the private key of a:    "))
b=int(input("Enter the private key of b:    "))

y1=int(pow(alpha,a,p))
y2=int(pow(alpha,b,p))

k1=int(pow(y2,a,p))
k2=int(pow(y1,b,p))

if(k1==k2):
    print("Common key is used:  ",k1)

else:
    print("Error")