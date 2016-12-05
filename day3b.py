# adventofcode 2016 day 3 part 2

lines = [line.rstrip('\n') for line in open('day3.txt')]
solution = 0
i = 1
Ta, Tb, Tc = [],[],[]

def is_valid(triangle) :
	a, b, c = False, False, False
	a = int(triangle[0]) + int(triangle[1]) > int(triangle[2])
	b = int(triangle[0]) + int(triangle[2]) > int(triangle[1])
	c = int(triangle[1]) + int(triangle[2]) > int(triangle[0])
	if (a and b and c) :
		return 1
	else :
		return 0

for line in lines :
	cols = [line[2:5].strip(), line[7:10].strip(), line[12:15].strip()]
	Ta.append(cols[0])
	Tb.append(cols[1])
	Tc.append(cols[2])

	if i >= 3 :
		solution += is_valid(Ta) + is_valid(Tb) + is_valid(Tc)
		Ta, Tb, Tc = [],[],[]	
		i = 0

	i+= 1

print(solution)