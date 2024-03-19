#dicktionary = A changable , unordered collection of unique key : valye pairs Fast beacuase they use hashing , allowing us to 
#              acess a value quickly 

capitals ={"India":"delhi",
           "usa":"washinton dc",
           "russia":"moscow"}#using curly  bracket same as the sets but different cause you can associate a value with another value

#print (capitals ["russia"])
#print (capitals["gemany"]) #since i dont have germanhy in my dictionary therefore will error
# to fix that i will
#print (capitals.get("Germany"))

#print(capitals.keys())
#print (capitals.values())
#print (capitals.items())

for key,value in capitals.items():
    print(key, value)