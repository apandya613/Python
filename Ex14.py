from sys import argv
script, user_name, play = argv
prompt = '--)'

print "Hi %s, I'm the %s script. and you are playing %r" %(user_name, script, play)
print "I'd like to ask you a few questions."
print "Do you like me %s?" %user_name
likes = raw_input(prompt)

print "where do you live %s?" %user_name
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print """
you said %r about liking me.
you live in %r. 
you have %r computer.
""" %(likes, lives, computer)