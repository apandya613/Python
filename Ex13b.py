from sys import argv

#I have created one with many arguments and skipping the one with less as it it same
script, name, age, height, weight, city = argv
print "hey %r you are %r years old %r tall %r heavy from %r " %(name, age, height, weight, city)

#there is the user input from with the sys argv
current_city = raw_input("Please give me the current city :")
print "hey %r you are %r years old %r tall %r heavy from %r currently in %r" %(name, age, height, weight, city, current_city)