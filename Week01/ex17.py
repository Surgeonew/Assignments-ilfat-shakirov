from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#
in_file = open(from_file)
indata = in_file.read()
print "The input file is %d bytes" % len(indata)
print "ready, hit Return to continue"
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Ok"
out_file.close()
in_file.close()
