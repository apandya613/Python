#assigns the string value to the variable x with the embaded string format.
x = "There are %d types of people." % 10
#assigns the string value to variable binary
binary = "binary"
#assigns the string value to variable do_not
do_not = "don't"
#declaring the variable y with the embaded string format. Added string into the string (1,2)
y = "Those who know %s and those who %s." % (binary, do_not)

#simply printing the variables x and y
print x
print y

#this line is tricky part where we have printed entire string object x it is not printing the string but the string object
print "I said: %r." % x
#this line is calling the string object and printing the actual string. Added string into the string (3) I believe there are just three.
print "I also said: '%s'." % y

#declaring a boolean variable with False value
hilarious = False
#this is just a string object
joke_evaluation = "Isn't that joke so funny?! %r"

#the print statement is printing the string object but it has string formatting where we printed the 'hilarious' which is boolean object
print joke_evaluation % hilarious

#declaring two strings
w = "This is the left side of..."
e = "a string with a right side."

#this statement is adding two string, well concatenate would be a better word for strings
print w + e
#in python "+" operator on sequences calls the concat function and it returns the concatenation of two sequences [1,2,3,4] + [5] will give [1,2,3,4,5]
a = [1,2,3]
b = [2,3,4,5]
print a + b #here it concatenate a and b