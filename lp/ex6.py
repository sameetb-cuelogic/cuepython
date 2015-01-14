
# -*- coding: utf-8 -*-

s = "Hey there! what should this string be?"

print s

print "Length of s is %d" % len(s)

print "Letter 'a' first occurs at %d" % s.index('a')

print "Count of 'a' is %d" % s.count('a')

print "First five characters: %s" % s[:5]
print "Next five characters: %s" % s[5:10]
print "Twelfth character is: %s" % s[11]
print "Last five characters: %s" % s[-5:]

print "Uppercase: %s" % s.upper()
print "Lowercase: %s" % s.lower()

print "Starts with 'Str': %s" % s.startswith("Str")
print "Ends with 'be?': %s" % s.endswith("be?")

print "First three words: %s" % s.split(' ')[:3]
