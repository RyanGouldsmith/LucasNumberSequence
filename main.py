#!/usr/bin/python 
import sys
def work_out_sequence(term):
    if (term == 0):
        return int(sys.argv[1]) 
    elif (term == 1 ):
        return int(sys.argv[2]) 
    else: return work_out_sequence(term-1)+ work_out_sequence(term-2)

if __name__ == "__main__":
    total = 0
    if (int (sys.argv[1]) > int(sys.argv[2])):
        for i in range (0, 20):
           total += work_out_sequence(i)
           print (work_out_sequence(i))
    print "Total sum of your lucas numbers are: %d" % total
