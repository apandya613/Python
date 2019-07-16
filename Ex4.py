cars = 100
space_in_a_car = 4.0 #the floating point number is not required here
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#If we want to find the minimum number of cars required, passengers/space_in_a_car space_in_a_car needs to be integer we can not break a car into half.
min_cars = passengers/space_in_a_car
print "we need atleast", min_cars, "to get all passengers."