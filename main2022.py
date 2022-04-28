import csv
from collections import defaultdict
import math
class Telephely:

	def __init__ (self,name,x,y,amount):
		self.name = name
		self.cord = tuple([int(x),int(y)])
		self.amount =  int(amount)

		self.distances = {}
		self.received = []

	def append_distance(self,name,dist):
		self.distances[name] = dist

class Map:
	def __init__(self):
		self.map = [["." for i in range(20)] for i in range(20)]
		
	def add(self,y,x):
		self.map[y][x] = "O"

	def output(self):
		with open("terkep.out", 'w') as out:
			for row in self.map:
				for char in row:
					out.write(char)
				out.write('\n')


def calculateDistance(cordx,cordy):
	return math.sqrt((cordx[0] - cordy[0])**2 + (cordx[1] - cordy[1])**2)

def elso_feladat(data):
	
	print("-1-")

	for row in data:
		counter = 0

		for i in row.name:
			if i.isdigit() and counter <= 3:
				counter += 1
			else:
				continue

		if counter == 3:
			print(row.name,":",row.cord)
			pass

def masodik_feladat(data):
	
	print("-2-")

	m = -1
	max_names = []
	for i in data:
		if m == i.amount:
			max_names.append(i.name)
		elif m < i.amount:
			max_names = []
			max_names.append(i.name)
			m = i.amount
		else:
			pass

	for name in max_names:
		print(name)

def harmadik_feladat(data):
	print("-3-")
	names = {i.name : [] for i in data}
	for row in data:
		string = row.name + ": "
		distances = dict(sorted(row.distances.items(), key = lambda item: item[1]))
		#print(row.name, "::: ",distances)
		for i,v in enumerate(distances.keys()):
			names[v].append(row.name)
			#string += v + ", "
			if i == row.amount -1: # mert 0-tol kezdodik
				break

	for n in names.keys():
		string = n + ": "
		for i in names[n]:
			string += i +", "
		print(string)


def otodik_feladat(data):
	print("-5-")

	x = 0
	y = 0
	x = round(sum([row.cord[0] for row in data])/len(data))
	y = round(sum([row.cord[1] for row in data])/len(data))
	suma = math.ceil(len(data)/2)
	emberek = sorted([tuple([calculateDistance(row.cord,tuple([x,y])),row.name]) for row in data])
	
	print("( ",x,y," )")
	print(suma, "galamb")
	separator = ', '
	print(', '.join([i[1] for i in emberek[:suma]]))
def main():

	data = []

	mapa = Map()

	with open("data.csv","r",encoding="UTF-8") as csvfile:
		reader = csv.reader(csvfile,delimiter=';')
		for ids,row in enumerate(reader):
			data.append(Telephely(row[0],row[1],row[2],row[3]))
			mapa.add(int(row[2])-1,int(row[1])-1)
	#calculate distances

	for i in range(0,len(data)-1):
		for j in range(i+1,len(data)):
			dist = calculateDistance(data[i].cord,data[j].cord)

			data[i].append_distance(data[j].name,dist)
			data[j].append_distance(data[i].name,dist)

	elso_feladat(data)
	masodik_feladat(data)
	harmadik_feladat(data)
	otodik_feladat(data)

	mapa.output()
if __name__ == "__main__":
	main()	
