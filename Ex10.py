tabby_cat = "\tI'm tabbed in."
persian_cat = "This is \n on line"
backslash = "There is the \\ printed in line"

fatcat = '''
\\     backslash 
\'     quotes 
\a     ASCII bell 
\b     ASCII backspace 
\f     ASCII formfeed 
\n     inline feed  
\r     ASCII carriage return
\t     tab
\v     vertical tab
\Oo   char with octal value
 '''
 
print tabby_cat
print persian_cat
print backslash
print fatcat

#saving in comment as this infinite loop can trouble
"""while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
"""
