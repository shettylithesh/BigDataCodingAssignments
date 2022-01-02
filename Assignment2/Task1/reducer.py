#!/usr/bin/env python3
import sys
vfile_path=sys.argv[1]


destination_list=list()
previous_source=-999  #initialized with very small number just for comparison

f=open(vfile_path ,'w')

for line in sys.stdin:
    source=line.split()[0]
    destination=line.split()[1]
    if(previous_source==source):
        destination_list.append(destination)
    else:
        if(len(destination_list)!=0):  #to tackle first line of mapper op
            print(previous_source,destination_list)
            f.write(previous_source +","+ "1")
            f.write("\n")
        destination_list=[]
        previous_source=source
        destination_list.append(destination)

print(previous_source,destination_list)    #to print last node of the graph
f.write(previous_source +" "+ "1")
f.write("\n")
