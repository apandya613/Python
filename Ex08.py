#here formatter is a string
formatter = "%r %r %r %r"

#printing the string with string format and %r is printing the integers
print formatter % (1, 2, 3, 4)
#all four string objects printed as it is
print formatter % ("one", "two", "three", "four")
#boolean variables printed as it is
print formatter % (True, False, False, True)
#the formatter string is going to be printed for each and every format parameter
print formatter % (formatter, formatter, formatter, formatter)
#The cheeky like "But it didn't sing." have single quote in it. So it is getting printed in the double quotes to distinguish the single quote in the string
print formatter % ("I had this thing.","That you could type up right.","But it didn't sing.","So I said goodnight.")