from sys import argv

script, filename = argv

print "let me open the file."
f = open(filename)
print f.read(10)
print f.readline()
#The below code is just for my satisfaction and lists are going to come in the upcoming lectures
a = f.readlines()
print a[0]
print a[1]