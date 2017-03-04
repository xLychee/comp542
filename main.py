import time

a = time.time()

k=0
c=15.0
while k<1000000:
    c=c**100
    c=c%500
    k+=1
print c
b=time.time()
print b-a

