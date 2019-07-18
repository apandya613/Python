print "I will now count my chickens:"

print "Hens", 25 + 30 / 6   #we can do simple mathematical operations while printing
print "Roosters", 100 - 25 * 3 % 4 #The modulo has lower precedence to the multiplication 

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6 #well python 2 is rounding the floating point numbers It should be 6.75 instead
#modulo have higher precedence to the addition
print "Is it true that 3 + 2 < 5 - 7?" #less-than as a string is not an operator

print 3 + 2 < 5 - 7 #less-than used to check condition and returns boolean value

#some more examples to check conditions using operators

print "What is 3 + 2?", 3 + 2 
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False." 

print "How about some more."

print "Is it greater?", 5 > - 2
print "Is it greater or equal?", 5 >= - 2
print "Is it less or equal?", 5 <= - 2