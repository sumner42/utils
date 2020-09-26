#!/usr/bin/python
########################################################################
# FILE: hello.py
#
# PURPOSE: Python Hello World program
#
# USAGE: hello.py
########################################################################
print("Hello Python world!")

# This didn't work
#print("Output from ps command:")
#with os.popen('ps -ef') as pse:
#    for line in pse:
#        print line

print("Loop with counter:")
colors = ["red", "green", "blue", "purple"]
i = 0
while i < len(colors):
    print(i, colors[i])
    i += 1
