print "how old are you?",
age = raw_input()
print "how tall are you?",
height = raw_input()
print "tell me ur weight.",
weight = raw_input()
print "so you're %r old, %r tall and %r heavy." % (age, height, weight)
#there was a very interesting output with 5'10" printed as 5\'10" 
#much interesting is when you enter 5'10 whithout double quote it uses double quote to store string and we get the output aswe expect
#the string is stored with escaping the special characters 
#if you use %s to print the string it will give you 5'10"
print "so you're %r old, %s tall and %r heavy." % (age, height, weight)

#i have found that we can print with the function aswell
number = int(raw_input("please enter an integer value :"))
