# adventofcode 2016 day 4
import operator
import collections

lines = [line.rstrip('\n') for line in open('day4.txt')]
solution = 0

def is_valid(room):
	tab_char = {}
	charlist = []
	sequences = room.split('-')[::-1]
	keys = sequences[0]
	checksum = keys.split('[')[1][:-1]
	sector_id = keys.split('[')[0]

	for sequence in sequences[1:] :
		for char in sequence :
			if char in tab_char :
				tab_char[char] += 1
			else :
				tab_char[char] = 1

	tab_char = collections.OrderedDict(sorted(tab_char.items(), key=operator.itemgetter(0)))
	sorted_tab = collections.OrderedDict(sorted(tab_char.items(), key=operator.itemgetter(1), reverse=True))

	calculated_checksum = [key for key, value in sorted_tab.items()]
	if calculated_checksum[:5] == list(checksum) :
		return int(sector_id)
	else :
		return 0

for room in lines :
	solution += is_valid(room)

print(solution)