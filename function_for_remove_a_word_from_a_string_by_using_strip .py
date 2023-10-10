def remove_and_strip(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()

this="    this is my string "
n=remove_and_strip(this,"my")
print(n)