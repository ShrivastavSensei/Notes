# set = collection which is unodered and unindexeds no duplicate values

utensils = {"fork","spoon","knife"}

dishes = {"bowl" , "plates", "cup"}
#utensils.add("napkin")
#utensils.remove ("fork")
#for x in  utensils:
 #   print (x)
#note the set function is unordered therefore faster than list or turple since it doesnot follow a order
    




#uniting the sets 

dinner_table = utensils.union(dishes)
print (dinner_table)
print (dishes.difference(utensils))
print (utensils.intersectoin(dishes))