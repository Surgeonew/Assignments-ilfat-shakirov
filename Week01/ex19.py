def cheesecrackers(shee_count, box_crackers):
    print "Y have %d chesses!" % shee_count
    print "Y have %d boxes of chackers" % box_crackers
    print "Man that's enougth for a party"
    print "Get a blanket.\n"
    
print "We can just give the function nambers directly:"
cheesecrackers(20, 30)

print "or, we can use variable from our script:"
A_O_cheese = 10
A_O_crackers = 50
cheesecrackers(A_O_cheese, A_O_crackers)

print "We can even do match inside too:"
cheesecrackers(10+30, 5+6)

print "And we can the 2, var and math:"
cheesecrackers(A_O_cheese+300, A_O_crackers+600)
