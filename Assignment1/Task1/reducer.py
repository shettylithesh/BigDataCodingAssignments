#!/usr/bin/env python3
import sys
#query_word = sys.argv[1]  
dictOp={ }
for line in sys.stdin:     #line is a tuple
    dictOp[int(line)] =dictOp.setdefault(int(line),0) + 1    

#sort_dictOp = {key:dictOp[key] for key in sorted(dictOp)}  #sorts based on key 
for key in sorted(dictOp.keys()):
    print(key, dictOp[key])

#for key,value in dictOp.items():
#    print(key,value)
