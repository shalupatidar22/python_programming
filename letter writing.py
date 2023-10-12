letter = ''' dear  <|NAME|>'
greeting..............
dateP: <|DATE|>'''

name=  input("enter your name")
date = input("enter date \n")
letter= letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>", date)
print(letter)