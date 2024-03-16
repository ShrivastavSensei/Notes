#loop control statements = change  a loops execution from its normal sequence

#break = used to terminte the loop entirely 
#continue = skips to next iteration of the loop
#pass = does nothing acts as placeholder

#example for break 
#while True :
 #   name = input ("your name?: ")
  #  if name !="":
   #     break

# example for contiuation = 
phone_number = "937-836-923"

for i in phone_number :
    if i == "-" :
        continue
    print(i ,end="")

#continue more like dont print 
#example for pass
#for i in range (1,21):
  #  if i == 13:
   #     pass
    #else:
     #   print(i)