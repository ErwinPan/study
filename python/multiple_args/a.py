def manyArgs(*arg):
          print "I was called with", len(arg), "arguments:", arg

manyArgs(1)
#          I was called with 1 arguments: (1,)

manyArgs(1, 2,3)
#          I was called with 3 arguments: (1, 2, 3)
