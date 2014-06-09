t = open('90052.txt', 'r')
name = '90052.txt'
import re
count = 0
r = re.compile('[0-9]')
for i in range(909):
	count += 1
	print count
	chk = t.read()
	f = chk.split(' ')
	for elem in f:
		if elem == 'comments' or elem == 'comment':
			count = 999999999999999
	print name 
	print chk
	nothing = ''.join(re.findall(r, chk))
	name = nothing+'.txt'
	t = open(name, 'r')
	
