import os
result=[]
columns=[]
example=[]
for line in open("cafe.fas.u",'r'):
        example.append(line.strip())
for taxa in example:
        first=taxa.split(':')[0]
        print first
        second=taxa.split(':')[1]
        print second
        if first in columns:
                result.append(second.strip())
        else:
                result.append('\n'+taxa.strip())
                columns.append(first.strip())
result=','.join(result)
open('result.csv','w').write(result)
os.system('sed -i "/^$/d" result.csv')
os.system('sed -i "s/,$//g" result.csv')