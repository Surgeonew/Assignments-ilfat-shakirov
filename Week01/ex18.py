def print_two(*args):
    arg1, arg2 = args
    print "a1: %r, a2: %r" % (arg1, arg2)

#ok

def print_two2(arg1, arg2):
    print "a1: %r, a2: %r" % (arg1, arg2)

def print_one(arg):
    print "arg: %r" % arg

def print_none():
    print "i got nothin!"

print_two("ilfat","gulsina")
print_two2("ilfat","gulsina")
print_one("gulsina")
print_none()

