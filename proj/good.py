import sys
M = []
namelist = []
f = open("rgzn.txt","r")
string = f.read()
lista = string.split('\n')
for i in range(0,len(lista)):
	num1 = lista[i].index(',')
	num2 = lista[i].index(']')
	listb = lista[i][num1+1:num2].replace(' ', '').split(',')
	# lista[i] = lista[i].split(',',1)
	namelist.append(lista[i][0:num1])
	# listb = lista[i][1][1:-1].split(',')
	M.append(listb)

num = len(M)
thr = 0.75 #we can set it
class node(object):
	def __init__(self, name):
		self.name = name
		self.children = []
		self.truchildren = []

def exec(mynode):
	max = -1
	index = -1
	if len(mynode.children) == 0:
		return 0
	for i in mynode.children:
		if int(M[mynode.name][i]) > max:
			index = i
			max = int(M[mynode.name][i])
	closet = node(index)
	mynode.truchildren.append(closet)
	mynode.children.remove(index)
	i = 0
	while(i<len(mynode.children)):
		if int(M[index][int(mynode.children[i])]) > int(M[int(mynode.children[i])][int(mynode.children[i])])*thr:
			closet.children.append(mynode.children[i])
			mynode.children.remove(mynode.children[i])
			i = i - 1
		i = i + 1
	if len(mynode.children) == 0:
		for j in mynode.truchildren:
			exec(j)
	else:
		exec(mynode)
java = node(0)
for i in range(1,num):
	java.children.append(i)

exec(java)

def printnode(mynode,fathernode):
	if fathernode == 0:
		print('root name is:' + namelist[mynode.name])
	else:
		print('father is ' + namelist[fathernode.name] + ': '+ namelist[mynode.name])
	for i in range(0,len(mynode.truchildren)):
		printnode(mynode.truchildren[i],mynode)

printnode(java,0)

print('*********')
print(namelist)