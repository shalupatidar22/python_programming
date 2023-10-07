#list comprehenssion
ls=[i for i in range(10) if i%2==0]
print(ls)

#dictionay comprehenssion
dict={i:f"items{i}" for i in range(10) if i%2==0}
print(dict)

# we can reverse dict by using dict comprehenssion
dic={value:key  for key , value in dict.items() }
print(dic)

#set comprehension
dress={dress for dress in ['dress1','dress2']}
print(dress)