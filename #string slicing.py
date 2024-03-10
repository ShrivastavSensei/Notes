#string slicing
#define- create a substring by extracting elements from another string
#          PART-1 -indexing[] | PART -2 - slice ()
#            [start:stop:step] ]
#PART -1
#ex
#name ="Shrivastav Sensei"
#first_name = name[0:10]
#last_name = name[11:17]
#funky_name = name[1:17:2 --- when i used step = 2 it  will start on 1 and end on 17 but  only print the second letter ex- hiatvsne
#print (first_name)
#reversed_name = name[::-1]

#print (last_name)
#print (funky_name)
#print (reversed_name) -- output iesneS vatsavirhS

#PART -2
#website = "http://google.com"

#slice = slice (7,-4)

#print(website[slice])``