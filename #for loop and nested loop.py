#
#for loop = a statement that willl execut its block of code 
#           limited amount of time 
#for i in range(10):
 #   print(i+1)

#import time

#for seconds in range (10,0,-1):
#    print (seconds)
#    time.sleep(1)
#print ("You are retarded")

 
#NESTED LOOPS = The inner loop will finnish all of tis iteration berfore finishing one iternation of the outer loop
rows = int(input ("how many rows?: "))
columm = int(input("how many columns?: "))
symbol = input("what sym?: ")

for i in range (rows):
    for j in range(columm):
        print(symbol , end="")
    print()