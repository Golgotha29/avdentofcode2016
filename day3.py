# adventofcode 2016 day 3

lines = [line.rstrip('\n') for line in open('day3.txt')]

solution = 0
a, b, c = False, False, False

for line in lines :
	triangle = [line[2:5].strip(), line[7:10].strip(), line[12:15].strip()]
	a = int(triangle[0]) + int(triangle[1]) > int(triangle[2])
	b = int(triangle[0]) + int(triangle[2]) > int(triangle[1])
	c = int(triangle[1]) + int(triangle[2]) > int(triangle[0])
	if a and b and c :
		solution += 1

print(solution)