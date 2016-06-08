print "you enter the dark room with two dors. Do you go trhougth door 1 or 2?"
door = raw_input("> ")
if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. take the cake"
    print "2. scream at the bear."
    bear = raw_input("> ")
    if bear == "1":
        print "The bear eats your face off"
    elif bear == "2":
        print "The bear legs your face off"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
elif door == "2":
    print "You state into the endless abyss at Cthulhu's retina."
    print "1. blueberries."
    print "2. yellow jacket clothespins."
    print "3. understanding revolvers yelling melodies."
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "your body survives powered by a mind of jello."
    else:
        print "the insanity rots your eyes into pool of muck."
else:
    print "you stumble around and fall on a knife and die"
    
