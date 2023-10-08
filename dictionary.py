d1 = {}
d2 = {"harry":"roti","shalu":"prathe","Roshni":"samosa","d":{"n":"not","r":"fine","u":"yes"}}
#d2["ankit"] = "junk food"
#d2[345] = "goli"
#d3 = d2.copy()
#del d3[345]
#print(d2)
#d2.update ({"leena":"moti"})
#print(d2)
print(d2.keys())
print(d2.items()) 
print(d2['harry'])   # for print particular element
print(d2.values())   # print the key of the dictionary

print(d2.get('harry2'))     # returns none as harry2 does not present in dic
