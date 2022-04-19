file = open("data.dat",'r')
Lines = file.readlines()
sum = 0
for line in Lines:
	if(line.count('1') % 2 == 0 or line.count('0') % 3 == 0):
		sum += 1
print(sum)
