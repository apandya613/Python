#importing the argv module from sys library
from sys import argv

#assigning command line arguments
script, filename = argv

#opening file
txt = open(filename)

#printing filename a CLA
print "here is ur file %r:" %filename
#printing the file content
print txt.read()

#asking user to enter filename
print "Type the filename again:"
#taking input
file_again = raw_input(">")

#again opening the file and printing the content
txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()
#there i wanted to test something
print open(filename).read()
#also wanted specific lines and stuff like that
print open(filename).readlines()[2]
#just a few letters...!
print open(filename).read(15)