#!/usr/bin/python

far = 0
step = 20 
for far in reversed(range (0,301,20)):
    cel = 5 * (far - 32) / 9
    print("%d\t%d" %(far, cel))