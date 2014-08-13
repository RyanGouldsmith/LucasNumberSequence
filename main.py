#!/usr/bin/python 
import sys
def work_out_sequence(term):
    if (term == 0):
        return int(sys.argv[1]) 
    elif (term == 1 ):
        return int(sys.argv[2]) 
    else: return work_out_sequence(term-1)+ work_out_sequence(term-2)

if __name__ == "__main__":
    for i in range (0, 20):
        print (work_out_sequence(i))
