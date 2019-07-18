from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
#with less arguments the error is that more than 1 value to unpack
#the argv is asking a total of 4 values including script name
#we give the script name to run but then we need to give 3 more values to unpack