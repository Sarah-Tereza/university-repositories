num=[]
i=0
while ( len (num)<6) :
    num.append(float(input("digite um numero:")))
print (num)

while (i  < len(num)):
    print(f"posição:{i}={num[i]}")
    i=i+1