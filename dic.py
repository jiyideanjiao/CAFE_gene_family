import sys
input=sys.argv[1]
output=sys.argv[2]
f=open(input,"r")
out=open(output,"w")
dic_file=open("specie.txt.u","r")
tmp=[]
tmp1=[]
for dic_file_line in dic_file:
	dic_file_line_new=dic_file_line.split(":")
	head=dic_file_line_new[0]
	tail=dic_file_line_new[1].strip()
	tmp.append(head)
	tmp1.append(tail)
dic=dict(zip(tmp,tmp1))
print (dic.keys)
for key in dic.keys():
	for line in f:
		head=line.split(":")[0]
		out.write("\n"+head+",")
		for key in dic:
			count=line.count(key)
			dic[key]=count
		for value in dic.values():
			out.write(str(value)+",")
