#543210******1234

def luhncheck(s):
	S = ''
	i = 0
	position = len(s)-1
	while  position >= 0:
		d = 1 + (position % 2 != 0)
		i = len(s) - position - 1
		S += str(int(s[i])*d)
		position -= 1	
	sum = 0
	for i in range(0,len(S)):
		sum += int(S[i])
	if sum % 10 == 0:
		return True
	
for i in range(10000000,10999999):
	s = '5432'+str(i)+'1234'
	if(int(s) % 123457 == 0 and luhncheck(s)):
		print(s)

		

