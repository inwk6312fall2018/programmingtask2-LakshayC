
#not working
from collections import Counter
mylist=[]
colw=[]
cole=[]
fcolw=[]
fcole=[]
finallist=[]
sorteddict1={}
sorteddict2={}
finaldic={}
with open("Crime.csv") as myfile:
	for line in myfile:		
		line1 = line.strip()
		line2 = line.split(',')		
		colw.append(line[-1]) 		#column 1 as Criem Name
		cole.append(line[-2]) 		#column 2 as Crime id
	colsw = dict((i, col2.count(i)) for i in col2) 		#column 3 as Crime Count

# built-in "Counter" function can also be used
#print(Counter(crime_count))

	col1nw2=zip(col2,col1)
	myries '''
	sorteddict1=dict(sorted((key1,val1) for key1,val1 in fcol1.items()))
	sorteddict2=dict(sorted((key2,val2) for key2,val2 in fcol2.items()))
#	print(sorteddict1)
#	print(sorteddict2)
#	print(type(sorteddict1))

	'''merge two dictonaries with 'crime name and id', 'id and count' based on key as 'crime id' '''
	for key in (sorteddict1.keys() or sorteddict2.keys()):
		if key in sorteddict1:
			finaldic.setdefault(key, []).append(sorteddict1[key])
		if key in sorteddict2:
			finaldic.setdefault(key, []).append(sorteddict2[key])
#	print(finaldic)

	'''Print output in table format'''
	print("{:<10} {:<23} {:<10}".format("Crime Id","Crime Name","Count"))
	for k,v in finaldic.items():
print("{:<10} {:<23} {:<10}".format(k,v[0],v[1]))
