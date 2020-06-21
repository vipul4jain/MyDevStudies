import os
fname='TestFile.csv'
fhand = open(fname)

for line in fhand:
    val=line.split(',')
    print (val)
    print (f"insert into Table ({val[0]} , {val[1]}, {val[2]}, {val[3].rstrip()} )")