# adventofcode 2016 day 4 part b
import operator
import collections

lines = [line.rstrip('\n') for line in open('day4.txt')]
solution = 0

def decrypt(chaine, cypher):
	alpha=list('abcdefghijklmnopqrstuvwxyz')
	decode = []
	for c in chaine :
		pos = alpha.index(c)
		n = pos + (cypher - 26*(cypher//26))
		if n > 25 :
			n = n - 26
		decode.append(alpha[n])
	return ''.join(decode)


def search(room):
	tab_char = {}
	charlist = []
	sequences = room.split('-')
	keys = sequences[len(sequences)-1]
	checksum = keys.split('[')[1][:-1]
	sector_id = keys.split('[')[0]
	decrypted_chain = ''
	for sequence in sequences[:-1] :
		decrypted_chain += decrypt(sequence,int(sector_id)) + ' '
	return decrypted_chain + str(sector_id)

for room in lines :
	s = search(room)
	if s.find('pole') > 0 :
		print(search(room))