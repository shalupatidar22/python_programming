def function(normal,*args, **kwargs):
    print(normal)
    for items in args:
        print(items)
    print(" know i would like to introduce some of our heroes")
    for key ,value in kwargs.items():
         print(f"{key} is a {value}")
  
har = ["harry","rohan","skill","shivali","shalu"]
normal = "i am a normal argument and the students are:"
kw = {"rohan":"monitor","harry":"fitness instructor",
      "skill":"argument","shivali":"bindass"}            
function(normal,*har,**kw)