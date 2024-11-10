import sys
number=int(sys.argv[1])
for i in range(0,number):
    if number%i==0:
        print(i,end=" ")
print()
        