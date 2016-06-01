cars = 40
space_in_a_car = 4.1
drivers = 10
passangers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capasity = cars_driven * space_in_a_car
average = passangers / cars_driven
print "There are", cars, "cars available"
print "There are", drivers, "drivers only"
print "There will be", cars_not_driven, " empty cars today"
print "We cal transport", carpool_capasity, "peeople today"
print "We have",passangers ," to carpool today"
print "We need to put",average,"in each car"
