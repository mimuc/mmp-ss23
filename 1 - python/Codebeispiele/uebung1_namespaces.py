def b():
   global x  # mind the difference with and without this statement
   x = 0
   print(x)
   print(locals())


x = 2

b()
print(x)
