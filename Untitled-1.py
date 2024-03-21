# scope  - the region that a variable is recongzied 
#          a variable is only available from inside the region its  created
#          A global and locally scoped versions of a variable can be created    

name = "shrivastav "# this is a global version of name 

def display_name():
    name = "sensei"  
    print (name) # this is a local scope the name can only be accesd inside the function
                   # our aim is to acess the name from outside the function
    
print(name)# tihis is gonna give error 



