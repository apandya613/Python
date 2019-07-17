name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

#a very good example to state importance of %r to show print no matter what important for debugging
import datetime

'%r' % datetime.datetime.now() #this is printing the object itself

'%s' % datetime.datetime.now() #this is calling the object and printing the return value

inch = 69
kg = 79
name = "akshay"
print "%r is %r cm tall %r kg" %(name, inch * 2.54, kg * 2.20)#here aswell the %r is printing string object
print "%s is %r cm tall %r kg" %(name, inch * 2.54, kg * 2.20)#when %s is calling the string object and printing the string

print "{0} is {1:.2f} cm tall {2:.4f} kg" .format(name, inch * 2.54, kg * 2.20)#string format using format function
