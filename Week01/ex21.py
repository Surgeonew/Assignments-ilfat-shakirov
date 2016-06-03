def add(a,b):
    print "adding %d+%d" % (a,b)
    return a + b
def sub(a,b):
    print "sub %d-%d" % (a,b)
    return a - b
print "Let's do some math with just functions!"
age = add(30,5)
height = sub(78,4)

print "Age:%d, Height:%d" %(age,height)
  
what = add(age, sub(height,age))
print "Thats bwcomes: ", what,"Can you do it ba hand?"
